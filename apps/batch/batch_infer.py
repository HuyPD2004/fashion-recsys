from application.inference.recommend import recommend_for_user

def batch():
    users = ["u1", "u2"]

    for u in users:
        recs = recommend_for_user(u)
        print(u, recs)

if __name__ == "__main__":
    batch()