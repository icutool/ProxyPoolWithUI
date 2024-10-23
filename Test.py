from util.xdbSearcher import XdbSearcher

def searchWithContent():
    # 1. 预先加载整个 xdb
    dbPath = "./util/ip2region.xdb";
    cb = XdbSearcher.loadContentFromFile(dbfile=dbPath)

    # 2. 仅需要使用上面的全文件缓存创建查询对象, 不需要传源 xdb 文件
    searcher = XdbSearcher(contentBuff=cb)

    # 3. 执行查询
    ip = "139.224.193.227"
    region_str = searcher.search(ip)
    ip_country = region_str.split("|")[0]
    print(ip_country)

    # 4. 关闭searcher
    searcher.close()
searchWithContent()