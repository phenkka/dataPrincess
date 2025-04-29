import pandas as pd
import matplotlib.pyplot as plt

class DisneyPrincessAnalysis:
    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)
        self._preprocess()

    def _preprocess(self):
        self.df = self.df.dropna(subset=["PopularityScore", "PrincessName"])
        self.df["PopularityScore"] = pd.to_numeric(self.df["PopularityScore"], errors='coerce')
        self.df["TikTokHashtagViewsMillions"] = pd.to_numeric(self.df["TikTokHashtagViewsMillions"], errors='coerce')
        self.df["BoxOfficeMillions"] = pd.to_numeric(self.df["BoxOfficeMillions"], errors='coerce')

    def filter_iconic(self):
        return self.df[self.df["IsIconic"] == "Yes"]

    def group_by_hair_color(self):
        hair_popularity = self.df.groupby("HairColor")["PopularityScore"].mean().sort_values(ascending=False)
        print("Average popularity by hair color:")
        print(hair_popularity.reset_index())
        return hair_popularity

    def plot_top5_popular(self):
        top5 = self.df.sort_values("PopularityScore", ascending=False).head(5)
        plt.figure(figsize=(10, 6))
        plt.barh(top5["PrincessName"], top5["PopularityScore"], color="skyblue")
        plt.title("Top 5 Princesses by Popularity")
        plt.xlabel("Popularity")
        plt.ylabel("Princess")
        plt.gca().invert_yaxis()
        plt.tight_layout()
        plt.savefig("graphs/top5_popularity.png")
        plt.clf()

    def plot_tiktok_views_distribution(self):
        plt.figure(figsize=(10, 6))
        plt.hist(self.df["TikTokHashtagViewsMillions"].dropna(), bins=20, color="lightcoral", edgecolor="black")
        plt.title("Distribution of TikTok Hashtag Views (in millions)")
        plt.xlabel("Millions of views")
        plt.ylabel("Number of princesses")
        plt.tight_layout()
        plt.savefig("graphs/tiktok_views_distribution.png")
        plt.clf()

    def plot_boxoffice_by_eye_color(self):
        plt.figure(figsize=(10, 6))
        self.df.boxplot(column="BoxOfficeMillions", by="EyeColor", grid=False, patch_artist=True)
        plt.title("Box Office Revenue by Eye Color")
        plt.suptitle("")
        plt.xlabel("Eye Color")
        plt.ylabel("Revenue (in millions)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("graphs/boxoffice_by_eye_color.png")
        plt.clf()

    def generate_all_plots(self):
        self.plot_top5_popular()
        self.plot_tiktok_views_distribution()
        self.plot_boxoffice_by_eye_color()

if __name__ == "__main__":
    analysis = DisneyPrincessAnalysis("disney_princess_popularity_dataset_300_rows.csv")
    analysis.group_by_hair_color()
    analysis.generate_all_plots()