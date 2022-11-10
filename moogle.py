#################################################################
# FILE : calculate_mathematical_expression
# WRITER : noam shabat , no.amshabat1 , 206515579
# EXERCISE : intro2cs2 ex6 2021
# DESCRIPTION: A simple search engine that crawl's the web.
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED: stackoverflow.com
# NOTES: ...
#################################################################
"""Import's: """
import copy
import pickle
import sys
from urllib.parse import urljoin

import bs4
import requests

"""Magick Variables: """
HTML = 'html.parser'


############################ part1 ###############################


def extract_list_of_links(index_file):
    """
    this func is reading the file and adds it to a list.
    :param index_file: the file that is being under reed.
    :return: a set that contains lines from the file.
    """
    f = open(index_file, 'r')
    index_file = list()
    for row in f.readlines():
        row = row.strip("\n")
        index_file.append(row)
    f.close()
    return index_file


def w_in_out_file(final_dict, out_file):
    """
    this func is transforming the output to the desired location.
    :param final_dict: the value that is bing transforming.
    :param out_file: the place of transfer.
    :return: none.
    """
    f = open(out_file, 'wb')
    pickle.dump(final_dict, f)
    f.close()

def crawl_page(soup, url_set, base_url):
    res = dict()
    for p in soup.find_all("p"):
        for link in p.find_all("a"):
            target = link.get("href")
            if target is None:
                continue
            if base_url in target:
                target = target.replace(base_url, "")
            if target in url_set:
                if target in res:
                    res[target] += 1
                else:
                    res[target] = 1
    return res


def get_soup(baseURL, pageURL):
    url = urljoin(baseURL, pageURL)
    response = requests.get(url)
    if not response:
        print("ERROR")
        return
    html = response.text
    return bs4.BeautifulSoup(html, "html.parser")


def get_set_of_urls(baseURL, indexFile):
    res = set()
    file = open(indexFile, 'r')
    for line in file.readlines():
        if baseURL in line:
            line = line.replace(baseURL, '')
        line = line.replace("\n", "")
        res.add(line)
    file.close()
    return res


def active_crawl(base_url, index_file, out_file):
    url_set = get_set_of_urls(base_url, index_file)
    traffic_dict = dict()
    for sub_page in url_set:
        soup = get_soup(base_url, sub_page)
        num_of_links = crawl_page(soup, url_set, base_url)
        if num_of_links != 0:
            traffic_dict[sub_page] = num_of_links
    w_in_out_file(traffic_dict, out_file)

############################part2###############################


def update_the_ranks(link_dic, rank_dic, rank_pages):
    """
    in this func we are two different dictionary and we want to return updated
    version of the rank dictionary.
    we are going to update the rank dictionary by chalking the ratio of the
    times one value is mentioning another value out of the sum of the value
    in total that is being mentioned.
    :param rank_pages: that is the rank of the page compared to the udders.
    :param link_dic: the dictionary that is contains all of the values.
    :param rank_dic:the dictionary that is being under update.
    :return:the updated rank dictionary.
    """
    total_sum_of_iteration = 0
    for page in link_dic:
        for row in link_dic[page]:
            total_sum_of_iteration += link_dic[page][row]
        for r in link_dic[page]:
            parcel_sum_of_iteration = link_dic[page][r]
            rank_dic[r] += rank_pages[page] * (
                    parcel_sum_of_iteration / total_sum_of_iteration)
        else:
            total_sum_of_iteration = 0
    for val in rank_dic:
        rank_dic[val] = rank_dic[val] - rank_pages[val]
    rank_pages = copy.deepcopy(rank_dic)
    return rank_pages, rank_dic


def active_rank(iteration, dict_file, out_file):
    """
    activates the rank call to check the rank of the pages.
    :param iteration: the amount of iteration that is being done.
    :param dict_file: a dictionary that hold the link connections.
    :param out_file: the return file after the changes.
    :return: None
    """
    rank_pages = dict()
    link_dic = read_from_pickle(dict_file)
    rank_dic = dict()
    for page_name in link_dic:
        rank_pages[page_name] = 1
        rank_dic[page_name] = 1
    for r in range(iteration):
        rank_pages, rank_dic = update_the_ranks(link_dic, rank_dic, rank_pages)
    w_in_out_file(rank_dic, out_file)


def read_from_pickle(dict_file):
    f = open(dict_file, 'rb')
    l_dict = pickle.load(f)
    f.close()
    return l_dict


############################part3###############################

def surfing_the_web(url):
    """
    this func is entering the site of the url that is gets.
    :param url: the url of the site.
    :return: the page of the site.
    """
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text, HTML)
    content = ""
    for p in soup.find_all("p"):
        content += p.text
        return content


def split_string_to_words(string):
    """
    cleaning and organizing the input and returns a list.
    :param string: the input of the func that gets an argument.
    :return: an organized list of input
    """
    clean_file = string.split(" ")
    cleand_list = []
    for word in cleand_list:
        cleand_list.append(word.replace("\n", "").replace("\t", ""))
    sort_words = sorted(clean_file)
    return sort_words


def active_words_dict(base_url, index_file, out_file):
    """
    this func is activating the active_words_dict call from the main.
    :param base_url: the url that is being used as a sours.
    :param index_file: a file that contains all of the information
    about that page and his data base html.
    :param out_file: the return file after the changes.
    :return: None
    """
    new_final_dic = dict()
    list_of_links = extract_list_of_links(index_file)
    for link in list_of_links:
        soup = get_soup(base_url, link)
        for p in soup.find_all("p"):
            p = p.text
            p = p.split(" ")
            for word in p:
                if word in new_final_dic:
                    if link in new_final_dic[word]:
                        new_final_dic[word][link] += 1
                    else:
                        new_final_dic[word][link] = 1
                else:
                    new_final_dic.update({word: {link: 1}})

    w_in_out_file(new_final_dic, out_file)


############################part4###############################


def get_soup2(base_url, link):
    """
    this func is getting a base url and relative url and return the correct
    url site.
    :param base_url: the base od the url link.
    :param link: the relative utl link og the site.
    :return: return the correct and full url site address.
    """
    temp_url = urljoin(base_url, link)
    response = requests.get(temp_url)
    html = response.text
    soup = bs4.BeautifulSoup(html, HTML)
    return soup


def calc_z(page, query, words_dict):
    """
    this func is calc the value of Z from the func active search.
    :param page:the page that is being examine onder the search fore the word.
    :param query: the word that is being checked.
    :param words_dict: a dict that contains all of the words.
    :return: the value ot the argument Z.
    """
    if page not in words_dict[query[0]]:
        return 0
    minimum_query = words_dict[query[0]][page]
    for word in query:
        if page not in words_dict[word]:
            return 0

        word_appearances = words_dict[word][page]
        if word_appearances < minimum_query:
            minimum_query = word_appearances

    return minimum_query


def val_of_the_page_as_tp(page_rank_tp):
    """
    the func is moving the from the cornet tuple that is being checked to the next one in line..
    :param page_rank_tp: the tuple of the current val in query.
    :return: next tuple in line.
    """
    return page_rank_tp[1]


def print_res(rank_pages):
    """
    this func is printing the result
    :param rank_pages: a page that contains all the ranks from the under
    pages that have the same word in them.
    :return: an print of the status of the results.
    """
    for page, rank in rank_pages:
        print(f"{page} {rank}")


def active_search(QUERY, RANKING_DICT_FILE, WORDS_DICT_FILE, MAX_RESULTS):
    """
    this func is activating the active_search call from the main.
    :param QUERY: the word that is being check for reference from the sites.
    :param RANKING_DICT_FILE: a dictionary that contains the ranking of
    the pages.
    :param WORDS_DICT_FILE: a dictionary that contains the whole variety
    of words that can be checked.
    :param MAX_RESULTS: that is a constant that gives the mex results that
    can be from the search function.
    :return: presents by "print" of all of the results from the search in the
    search engine.
    """
    words_dict = read_from_pickle(WORDS_DICT_FILE)
    rank_dict = read_from_pickle(RANKING_DICT_FILE)
    query = split_string_to_words(QUERY)
    for word in query:
        if word not in words_dict:
            query.remove(word)
    rank_pages = []
    for page in rank_dict:
        Z = calc_z(page, query, words_dict)
        if Z == 0:
            continue
        else:
            Y = rank_dict[page]
            rank = Z * Y
            rank_pages.append((page, rank))
    rank_pages.sort(key=val_of_the_page_as_tp, reverse=True)
    if len(rank_pages) <= MAX_RESULTS:
        for page, rank in rank_pages:
            print(f"{page} {rank}")
    else:
        for page, rank in rank_pages[:MAX_RESULTS]:
            print(f"{page} {rank}")
    return


def main(arg):
    """
    this func is the main func that activates the hole programme according
    to the desired request.
    :return: the desired request according to the argument that has bing
    implemented to the commend line.
    """
    if 'crawl' == arg[1]:
        BASE_URL = arg[2]
        INDEX_FILE = arg[3]
        OUT_FILE = arg[4]
        active_crawl(BASE_URL, INDEX_FILE, OUT_FILE)

    elif 'page_rank' == arg[1]:
        ITERATIONS = arg[2]
        DICT_FILE = arg[3]
        OUT_FILE = arg[4]
        active_rank(int(ITERATIONS), DICT_FILE, OUT_FILE)

    elif 'words_dict' == arg[1]:
        BASE_URL = arg[2]
        INDEX_FILE = arg[3]
        OUT_FILE = arg[4]
        active_words_dict(BASE_URL, INDEX_FILE, OUT_FILE)

    elif 'search' == arg[1]:
        QUERY = arg[2]
        RANKING_DICT_FILE = arg[3]
        WORDS_DICT_FILE = arg[4]
        MAX_RESULTS = int(arg[5])
        active_search(QUERY, RANKING_DICT_FILE, WORDS_DICT_FILE, MAX_RESULTS)

    return


def right_results_txt(list_of_ranked_pages):
    file = open("results.txt", "a")
    for page, rank in list_of_ranked_pages:
        file.write(f"{page} {rank}\n")
    file.write("*" * 10 + "\n")
    file.close()


if __name__ == "__main__":
    main(sys.argv)
