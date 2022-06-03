import csv
import pandas as pd

def available_words(ens_domains, valid_words):
  unused_ens = valid_words.difference(ens_domains)
  unused_lst = list(unused_ens)
  unused_lst.sort(key=lambda item: (len(item), item))
  return(unused_lst)

def run(file):
  df_ens = pd.read_csv('registered_ens.csv')
  df_dict = pd.read_csv(file)

  ens_series = pd.Series(df_ens['domain'])
  dict_series = pd.Series(df_dict['words'])

  ens_set = set(ens_series)
  dict_set = set(dict_series)

  avail = available_words(ens_set, dict_set)
  if 'TRUE' in avail: avail.remove('TRUE') # not sure why this appearing in results
  if 'FALSE' in avail: avail.remove('FALSE') # not sure why this appearing in results

  with open('unregistered_' + file, "w+") as f:
    writer = csv.writer(f)
    for val in avail:
      if len(val)>=3: # possible to change
        writer.writerow([val])


# current options - sowpods.csv, forbes.csv, baby_names_over_100_2021.csv, pro_athletes.csv, frequent_words.csv
file = 'frequent_words.csv' #change file name to change what we're looking for
run(file)