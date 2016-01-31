import googlemaps
import csv
import pandas as pd

def geo_lookup(location_df):
    # read in API key
    with open("api_key.txt", "r") as file:
        api_key = file.read()
    gmaps = googlemaps.Client(key=api_key)
    # TODO rate handling
    # TODO iterate through df
    # TODO recreate df
    geocode_result = gmaps.geocode('General Mills Headquarters, MN')


def read_raw_data(file_opts):
    file_name = file_opts[0]
    # offset header by 1 since most people will look at it in excel
    header_row = int(file_opts[1]) - 1
    sheet_name = file_opts[3]

    # determine how to handle the file based on extension
    file_path = 'INPUT/' + file_name
    if file_name.endswith('.csv'):
        # process comma delimited
        data_df = pd.read_csv(file_path, sep=',', header=header_row)
    elif file_name.endswith('.tsv'):
        # procss tab delimited
        data_df = pd.read_csv(file_path, sep='\t', header=header_row)
    elif file_name.endswith('.xlsx') or file_name.endswith('.xls'):
        # process excel sheet
        data_df = pd.read_excel(file_path, sheetname=sheet_name, header=header_row)
    else:
        # TODO raise exception here
        print(file_name, "has an unknown extension, skipping. Only csv, tsv, xls and xlsx are supported.")
    return data_df


if __name__ == "__main__":
    # read in the input options and process through each one
    with open("Input_Options.csv") as input_opts_file:
        reader = csv.reader(input_opts_file, delimiter=',')
        # skip the headers
        next(reader, None)
        # initialize output dataframe
        input_names = []
        # iterate over all files in input_options.csv
        for file_opts in reader:
            file_df = read_raw_data(file_opts)
            column_name = file_opts[2]
            school_names = file_df[column_name].str.lower()
            unique_names = pd.unique(school_names).tolist()
            for name in unique_names:
                input_names.append(name.strip())
        unique_input_names = set(input_names)
        print(unique_input_names)





# perform lookup, only those not cached, rate limit
# perform join
# write out copy of data with geolocation
