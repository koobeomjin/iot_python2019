# [참고사항]
# - API 호출수 25,000회/일 로 제한
# - 한번 호출에 최대 100개 검색
# - 한번 실행에 최대 1000개까지 기사 검색
import urllib.request
import datetime
import json

app_id='42MIKrlzhEuojaVxOrm4' #발급한 ID
app_pw='4FFS5gygSd' #발급한 PW

def get_request_url(url):
    req=urllib.request.Request(url)
    req.add_header('X-Naver-Client-Id',app_id)
    req.add_header('X-Naver-Client-Secret',app_pw)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print('[%s] Url:%s => Request Success' % (datetime.datetime.now(),url))
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print('[%s] Error for URL: %s'%(datetime.datetime.now(),url))
        return None

def getNaverSearchResult(sNode,search_text,page_start,display):
    base = 'https://openapi.naver.com/v1/search'
    node = '/%s'%sNode
    parameters = '?query=%s&start=%s&display=%s'%(urllib.parse.quote(search_text),page_start,display)
    url = base + node + parameters
    retData = get_request_url(url)

    if (retData == None):
        return None
    else:
        return json.loads(retData)

def getPostData(post,jsonResult):

    title = post['title']
    description = post['description']
    link = post['link']

    pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %y %H:%M:%S+0900')
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')

    jsonResult.append({'title':title, 'description':description,'pDate':pDate})
    return

def main():
    jsonResult = []

    sNode = 'blog'
    search_text = '아베'
    display_count = 10

    jsonSearch = getNaverSearchResult(sNode,search_text,1,display_count)

    nStart = 1
    for index in range(10):
        if index > 0:
            nStart += 100
        jsonSearch = getNaverSearchResult(sNode, search_text, nStart, display_count)
        index = index + 1
        for post in jsonSearch['items']:
            getPostData(post, jsonResult)

    with open('%s_naver_%s.json' % (search_text, sNode), 'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

    print('%s_naver_%s.json SAVED' % (search_text, sNode))

if __name__ == '__main__':
    main()