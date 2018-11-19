import datetime
class Comment:

    def __init__(self):
        self.commentList = []         

    def add_comment(self, aurthor, message):
        comment = {
            'comment_id': len(self.commentList) + 1,
            'aurthor': aurthor,
            'message': message,
            'comment_date': datetime.datetime.now()
        }
        self.commentList.append(comment)
        return comment

    def edit_comment(self, comment_id, aurthor, message):
        for comment in self.commentList:
            if comment.__dict__['comment_id'] == comment_id:
                if comment['aurthor'] == aurthor:
                    comment['message'] = message
                    return comment
                return 'only an aurthor can edit his/her comment'
        return 'comment not found'

    def delete_comment(self, comment_id, aurthor):
        for comment in self.commentList:
            if comment['comment_id'] == comment_id:
                if comment['aurthor'] == aurthor:
                    self.commentList.remove(comment)
                    return comment
                return 'only an aurthor can delete his/her comment'
        return 'comment not found'

    def view_comment(self):
        return self.commentList
 

if __name__ == '__main__':
     Comment().add_comment('a', 'b')