from load_csv import load
import matplotlib.pyplot as plt

def main():
    income_data = load('income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
    life_exp_data = load('life_expectancy_years.csv')
    year = '1900'
    print(life_exp_data)
    x = income_data[year].apply(lambda x: float(x[:-1]) * 1e3 if isinstance(x, str) and x.endswith('k') else
                                float(x))
    y = life_exp_data[year]
    check = x.notna() & y.notna()
    fix, ax = plt.subplots()
    ax.scatter(x[check], y[check])
    ax.set_title(year)
    ax.set_xlabel('Gross Domestic product')
    ax.set_ylabel('Life Expectancy')
    ax.set_xscale('log')
    ax.set_xticks([300, 1000, 10000])
    ax.set_xticklabels(['300', '1k', '10k'])
    plt.show()

if __name__ == '__main__':
    main()