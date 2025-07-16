from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def get_numeric_values(data, country: str):
    new_data = data.loc[data['country'] == country].drop(columns='country').iloc[0][:-50]
    new_data = new_data.apply(lambda x: float(x[:-1]) / 1e3 if x.endswith('k') else
                                        float(x[:-1]) if x.endswith('M') else
                                        float(x))
    return new_data

def main():
    data = load('population_total.csv')
    country = 'Finland'
    another_country = 'Italy'

    country_data = get_numeric_values(data, country)
    another_country_data = get_numeric_values(data, another_country)

    years = country_data.index.astype(int)

    fig, ax = plt.subplots()
    ax.plot(years, country_data, label=country, color='green')
    ax.plot(years, another_country_data, label=another_country, color='blue')

    ax.set_yticks([1, 3, 5, 10, 20, 40, 60])
    ax.set_xticks(range(1800, 2050, 40))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y:.1f}M'))

    ax.set_title('Population Projections')
    ax.set_xlabel('Year')
    ax.set_ylabel('Population')

    handles, lables = ax.get_legend_handles_labels()
    ax.legend(handles[::-1], lables[::-1], loc='upper left')

    ax.grid(True)
    plt.show()

if __name__ == '__main__':
    main()