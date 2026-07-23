import matplotlib.pyplot as plt
import os


class ChartTool:

    def bar_chart(self, dataframe):

        # Folder automatically create hoga
        os.makedirs("data", exist_ok=True)

        status_count = dataframe["Availability"].value_counts()

        plt.figure(figsize=(6, 4))
        plt.bar(status_count.index, status_count.values)

        plt.title("Book Availability")
        plt.xlabel("Availability")
        plt.ylabel("Count")

        plt.tight_layout()

        os.makedirs("charts", exist_ok=True)

        plt.savefig("charts/availability_bar.png")

        plt.close()

    def price_chart(self, dataframe):

        prices = dataframe["Price"].str.replace("£", "", regex=False).astype(float)

        plt.figure(figsize=(6, 4))
        plt.hist(prices, bins=8)

        plt.title("Price Distribution")
        plt.xlabel("Price (£)")
        plt.ylabel("Books")

        plt.tight_layout()

        os.makedirs("charts", exist_ok=True)

        plt.savefig("charts/price_distribution.png")

        plt.close()