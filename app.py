import instaloader

# Membuat instance Instaloader
ig = instaloader.Instaloader()

# Meminta input username dari pengguna
username = input("Masukkan username Instagram: ")

# Mendapatkan objek profil dari username
try:
    profile = instaloader.Profile.from_username(ig.context, username)
except instaloader.exceptions.ProfileNotFound:
    print(f"Username '{username}' tidak ditemukan.")
    exit()

# Mengunduh semua postingan dari akun tersebut
posts = profile.get_posts()

# Mengunduh setiap postingan
for post in posts:
    try:
        ig.download_post(post, target=f"{username}_posts")
    except instaloader.exceptions.QueryReturnedNotFoundException:
        print(f"Post {post.shortcode} tidak dapat diunduh.")
        continue