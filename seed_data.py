from django.contrib.auth.models import User
from apps.demo.models import Post, Comment
from django.utils import timezone
from datetime import timedelta
import random

def create_sample_data():
    # Create sample users
    users = []
    usernames = ['john_doe', 'jane_smith', 'bob_wilson', 'alice_brown', 'charlie_davis']
    
    for username in usernames:
        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                'email': f'{username}@example.com',
                'password': 'password123'
            }
        )
        users.append(user)
    
    # Create sample posts
    posts = []
    post_contents = [
        "Just launched my new project! 🚀 Super excited to share it with everyone!",
        "Beautiful sunset at the beach today. Nature never fails to amaze me. 🌅",
        "Great team meeting today. The future looks promising! 💼",
        "New coffee shop discovery - their lattes are amazing! ☕",
        "Working on some exciting features for our app. Stay tuned! 💻",
        "Just finished reading an amazing book. Highly recommend! 📚",
        "Weekend hiking adventures with friends! 🏔️",
        "Celebrating 5 years at the company today! 🎉",
        "New recipe experiment turned out perfect! 🍳",
        "Tech conference was mind-blowing! So much to learn! 🤓"
    ]
    
    base_time = timezone.now()
    
    for i, content in enumerate(post_contents):
        post = Post.objects.create(
            user=random.choice(users),
            text=content,
            timestamp=base_time - timedelta(days=i)
        )
        posts.append(post)
    
    # Create sample comments
    comment_contents = [
        "Great post! 👍",
        "Thanks for sharing!",
        "This is awesome!",
        "Couldn't agree more.",
        "Very insightful!",
        "Keep up the great work!",
        "Interesting perspective.",
        "Looking forward to more!",
        "Well said! 🎯",
        "This made my day!",
        "Totally relate to this.",
        "You nailed it!",
        "Inspiring! ✨",
        "Perfect timing!",
        "This is exactly what I needed to hear."
    ]
    
    for post in posts:
        # Create 5-8 comments per post
        num_comments = random.randint(5, 8)
        for j in range(num_comments):
            Comment.objects.create(
                post=post,
                user=random.choice(users),
                text=random.choice(comment_contents),
                timestamp=post.timestamp + timedelta(hours=random.randint(1, 24))
            )