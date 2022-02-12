import pandas as pd


def zero_one(ch):
    """
    changes chars M and m to 1

    :param ch: char that we need to change

    :return: 1 or 0 instead og char
    """
    if (ch == 'M') | (ch == 'м'):
        return 1
    else:
        return 0


def init():
    """
    initialisation

    :return:
    df : pandas.DataFrame
        Data frame from titanic_with_labels.csv
    """
    df = pd.read_csv('titanic_with_labels.csv', sep=' ')
    return df


def sex_filter(df):
    """
    delete series without indicated sex

    parameters
    ----------
    df : pandas.DataFrame
        Data frame to work with

    Returns
    ----------
        Data frame without not indicated sex
    """
    df = df[(df.sex != '-') & (df.sex != 'не указан')]


def change_sex_to_numbers(df):
    """
    changes male to 1 and female to 0

    parameters
    ----------
    df : pandas.DataFrame
        Data frame to work with

    Returns
    ----------
        'sex' column with 1 and 0 instead of male and female
    """
    df.sex = df.sex.map(zero_one)


def change_unspecified_rows(df):
    """
    changes unspecified rows to max number of row

    parameters
    ----------
    df : pandas.DataFrame
        Data frame to work with

    Returns
    ----------
        Data frame with all rows indicated
    """
    df.row_number = df.row_number.fillna(df.row_number.max())


def change_ejection_to_mean(df):
    """
    changes ejections of liters_of_drunk to mean value of this parameter

    parameters
    ----------
    df : pandas.DataFrame
        Data frame to work with

    Returns
    ----------
        liters_of_drunk column with changed ejections
    """
    df_helper = df[(df['liters_drunk'] < 6) | (df['liters_drunk'] >= 0)]
    mean = df_helper['liters_drunk'].mean()
    df.liters_drunk = df.liters_drunk.mask((df.liters_drunk < 0) | (df.liters_drunk > 10), mean)


def main():
    df = init()
    sex_filter(df)
    change_sex_to_numbers(df)
    change_unspecified_rows(df)
    change_ejection_to_mean(df)

    print(df)


if __name__ == "__main__":
    main()
