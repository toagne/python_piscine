import matplotlib.pyplot as plt
from load_csv import load

def main():
    data = load("life_expectancy_years.csv")
    country = 'France'
    country_data = data.loc[data['country'] == country]
    values = country_data.drop(columns='country').iloc[0]
    # print(values)
    values.plot(title=f'{country} life expectancy Projections',
                xlabel='Year', ylabel='Life Expectancy')
    plt.show()
    # print(country_data)
    # arr_data = country_data.to_numpy()
    # # print(arr_data)
    # arr_data = arr_data[0, 1:]
    # years = np.arange(1800, 2101)
    # # print(years)
    # fig, ax = plt.subplots()
    # ax.plot(years, arr_data)
    # ax.set_title(f'{country} life expectancy Projections')
    # ax.set_xlabel('Year')
    # ax.set_ylabel('Life Expectancy')
    # plt.show()


if __name__ == '__main__':
    main()