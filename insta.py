#pip install instaloader
import instaloader
ig = instaloader.Instaloader()
dp = input("Enter the user name")
ig.download_profile(dp, profile_pic_only = True)
