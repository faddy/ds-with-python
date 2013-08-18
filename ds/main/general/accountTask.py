#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
accountTask
~~~~~~~~~~~~~

Keep cache of account_id: account_guid mapping.
refreshed at regular intervals.

:copyright: Syncapse
"""
__author__ = 'Sameer Thakur (s.thakur@syncapse.com)'

import settings
import logging
import threading
from threading import Thread
from datetime import datetime
import time

from metadata.db_entities import DbEntities
from network_api.data_sources import DataSources
import network_api.constants as constants

logger = logging.getLogger(__name__)


# Module Constants
__is_active__ = False

# Global Cache to store {account_id:account_guid} mapping
__account_guid_cache__ = {}
lock = threading.Lock()

#interval
# NETWORKS_LIST = [DataSources.MS_ADCENTER, DataSources.GOOGLE_ADWORDS, DataSources.FACEBOOK]
NETWORKS_LIST = [DataSources.FACEBOOK]
REFRESH_INTERVAL = settings.ACCOUNT_TASK_REFRESH_INTERVAL * 60
NETWORK_RETRY = 1



def start():
    """ Entry point to start account refresh job task
    """
    global __is_active__
    if not __is_active__:
        __is_active__ = True
        task_thread = Thread(target=refresh_accounts_job)
        task_thread.daemon = True
        task_thread.start()


def stop():
    """Threading worker stopper..
    """
    global __is_active__
    __is_active__ = False


def refresh_accounts():
    """ Calls remote BLL service for all network accounts and re-create account id - guid cache
    """
    try:
        db = DbEntities()
        local_cache = {}
        retry_refresh = NETWORK_RETRY
        while (retry_refresh > 0):
            try:
                for network_id in NETWORKS_LIST:
                    logger.debug('Refreshing account_cache for network id {0}'.format(network_id))
                    accounts = db.get_accounts_by_source(network_id,constants.S2N_MODE)
                    logger.debug('Refreshing account_cache response received')
                    if accounts:
                        for account in accounts:
                            account_id = account.id
                            guid = account.guid
                            if isinstance(guid, unicode):
                                guid=guid.encode('utf-8')
                            local_cache[str(account_id)] = guid
                    else:
                        logger.debug('No accounts found for network id: {0} from bll'.format(network_id))
                global __account_guid_cache__
                __account_guid_cache__ = local_cache.copy()
                logger.debug('Account Cache Content {0}'.format(__account_guid_cache__))
                logger.debug('Finished refreshing account_cache with total {0}  accounts.'.format(len(local_cache)))

                retry_refresh = 0
            except Exception as e:
                if retry_refresh == 0:
                    logger.exception(
                        'Retry limit exceeded for account cache refresh exiting current cycle. error:{0}'.format(e))
                else:
                    retry_refresh -= 1
                    logger.exception('Exception in doing account refresh. error:{0}'.format(e))
    except Exception as e:
        logger.error("Problem encountered while refreshing account cache")


def refresh_accounts_job():
    """ Job to refresh account cache at regular intervals
    """
    global __is_active__
    while __is_active__:
        logger.debug('Starting account refresh job.')
        with lock:
            refresh_accounts()
        current_time = time.time()
        next_interval = time.strftime('%H:%M', time.localtime(current_time + REFRESH_INTERVAL))
        logger.debug('Next refresh cycle after {0} minutes at {1}.'.format(REFRESH_INTERVAL, next_interval))
        time.sleep(REFRESH_INTERVAL)
    logger.debug('Exiting account refresh task job')


def get_account_guid(account_id):
    """ Get account guid for a given account id
        Args:
          account_id : account id.
        Returns:
          guid : Account guid.
        @todo add some error handling if the guid is not found. right now, we get confusing errors.
    """
    try:
        logger.debug("Retrieving account guid for id: {0}".format(account_id))
        with lock:
            guid = __account_guid_cache__.get(str(account_id))
            logger.debug('Get Account[Account Cache Content] {0}'.format(__account_guid_cache__))
            if not guid:
                logger.debug("Missing Guid retrying refresh accounts: {0}".format(account_id))
                refresh_accounts()
                guid = __account_guid_cache__.get(str(account_id))
        logger.debug("Account guid for id: {0} guid:{1}".format(account_id, guid))
        return guid
    except Exception as e:
        logger.exception("Problem encountered while retrieving account guid for id: {0}".format(account_id))



if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s')
    start()
    print get_account_guid(31920)
    print __account_guid_cache__
