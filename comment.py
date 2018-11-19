import datetime


class Comment:

    commentList = []

    def add_comment(self, author, message):
        comment = {
            'comment_id': len(Comment.commentList) + 1,
            'author': author,
            'message': message,
            'comment_date': datetime.datetime.now()
        }
        self.commentList.append(comment)
        return comment

    def edit_comment(self, comment_id, author, message):
        for comment in Comment.commentList:
            if comment.__dict__['comment_id'] == comment_id:
                if comment['author'] == author:
                    comment['message'] = message
                    return comment
                return 'only an author can edit his/her comment'
        return 'comment not found'

    def delete_comment(self, comment_id, aurthor):
        for comment in Comment.commentList:
            if comment['comment_id'] == comment_id:
                if comment['author'] == aurthor:
                    Comment.commentList.remove(comment)
                    return comment
                return 'only an aurthor can delete his/her comment'
        return 'comment not found'

    def view_comment(self):
        return Comment.commentList
