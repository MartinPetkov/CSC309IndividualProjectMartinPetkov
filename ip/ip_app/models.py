from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=254, null=False)
    password = models.CharField(max_length=254, null=False)

    def __str__(self):
        return '[user_id: ' + str(self.user_id) + \
                '; email: ' + self.email + ']'


class Idea(models.Model):
    INDUSTRIES = (
        ('H', 'Health'),
        ('T', 'Technology'),
        ('E', 'Education'),
        ('F', 'Finance'),
        ('R', 'Travel'),
    )

    idea_id = models.AutoField(primary_key=True)
    submittor_id = models.ForeignKey(User)
    submission_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=50, null=False)
    industry = models.CharField(max_length=50, null=False, choices=INDUSTRIES)
    description = models.TextField(null=False)
    keywords = models.TextField(null=False)
    rating = models.IntegerField(default=0, null=False)

    def __str__(self):
        return '[idea_id: ' + str(self.idea_id) + \
                '; title: ' + self.title + \
                '; industry: ' + self.industry + \
                '; description: ' + self.description + \
                '; keywords: ' + self.keywords + \
                '; rating: ' + str(self.rating) + ']' \


class UserLike(models.Model):
    LIKE_DISLIKE = (
        (1, 'Like'),
        (0, 'Neutral'),
        #(-1, 'Dislike'),
    )

    user_id = models.ForeignKey(User)
    idea_id = models.ForeignKey(Idea)
    like_dislike = models.IntegerField(default=0, null=False, choices=LIKE_DISLIKE)

    def __str__(self):
        return '[user_id: ' + str(self.user_id) + \
                '; idea_id: ' + str(self.idea_id) + \
                '; like_dislike: ' + str(self.like_dislike) + ']'
