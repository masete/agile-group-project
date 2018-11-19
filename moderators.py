from comment import Comment
class Moderators(Comment):
    """
    class to define the functions performed by a moderator
    """

    def delete_comment_if_moderator(self,comment_id, author):
        Comment().delete_comment(comment_id, author)


moderator = Moderators()
if __name__ == "__main__":
    print(moderator.delete_comment_if_moderator(2, "Davis Keneth"))
            
                
            




