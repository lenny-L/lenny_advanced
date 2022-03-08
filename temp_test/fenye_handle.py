# -*- coding: utf-8 -*-
# @Time    : 2021/10/25 10:52
# @Author  : lenny
# @desc    :
import json
import requests


@crud.route('/list/paging', methods=['POST'])
def list_paging():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    data_count = len(list)
    # 对list进行分页处理
    currentPage = int(params(request=request, key='page', default=1))
    limit = int(params(request=request, key='limit', default=2))
    if (int(data_count % limit) == 0):
        pageCount = int(data_count / limit)
    else:
        pageCount = int(data_count / limit) + 1
    start_index = (currentPage - 1) * limit
    last_limit = 9999
    if currentPage == pageCount:
        last_limit = data_count % limit  # 最后一页的数据条数
    if last_limit != 9999:
        limit = last_limit
        end_index = start_index + limit
    end_index = start_index + limit
    list = list[start_index:end_index]
    return json.dumps(dict(
            count=data_count,
            pageCount=pageCount,
            currentPageLimit=limit,
            data=list,
            currentPage=currentPage
        ))