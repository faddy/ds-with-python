import json

def get_json(i):
    if i==1:
        return '''{
"values": [
            {
               "value": 0,
               "end_time": "2013-03-23T07:00:00+0000"
            }
         ]
}'''
    else:
        return '''{
"values": [
            {
               "value": 0,
               "end_time": "2013-03-23T07:00:00+0000"
            }
         
}'''


def throws_IOError(i):
    if i==1: 
        return 'this is response'
    else:
        raise IOError()

def throws_ValueError(i):
    if i==1:
        return 'this is json response'
    else:
        raise ValueError()

def test1(ctr):
    while(ctr>0):
        print 'try #', ctr
        response = None
        try:
            response = throws_IOError(1)
        except Exception as e:
            raise e
        else:

            json_str = get_json(0)
            try:
                json_response = json.loads(json_str)
            except ValueError, e:
                print "there was value error"
                ctr -= 1
                continue
            else:
                return json_response

        finally:
            if response: print "response is closed"


test1(3)

