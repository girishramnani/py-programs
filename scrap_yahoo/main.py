__author__ = 'Girish'


def find_next(past_comment,past_title,past_author):

    comment = past_comment.find_next("p","mb-text-full")
    title = past_title.find_next("a","mb-message-title")
    author = past_author.find_next("span","mb-by")

    return comment,title,author


def get_scrap_data(htmlpages):

    for page in htmlpages:
        output = bs4.BeautifulSoup(page,"lxml")

        title = output.find("a","mb-message-title")
        author = output.find("span","mb-by")
        comment = output.find("p","mb-text-full")


        while any([comment,title,author]):


            comment_data = comment.text
            title_data = title.text
            author_data = author.a.strong.text


            print(comment_data)
            print(title_data)
            print(author_data)
            print()


            comment,title,author = find_next(comment,author,title)

