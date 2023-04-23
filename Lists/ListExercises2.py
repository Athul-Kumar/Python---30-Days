

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Q-1

# sorting

ages.sort()

#  max and min ages

max_age = max(ages)
print(max_age)
min_age = min(ages)
print(min_age)

#  Q-2
# add max and min age again to list
ages.extend([max_age, min_age])
print(ages)

# Q-3
import statistics
median_age = statistics.median(ages)
print(median_age)

# another method

median_age = ages[5] + ages[6]
print(median_age/2)

# Q-4
# average of ages

sum_of_ages = sum(ages)
total_numbs = len(ages)
average_age = sum_of_ages / total_numbs
print(average_age)

# another method

sum_of =0
for age in ages:
    sum_of += age

total = len(ages)

average = sum_of / total
print(average)

# Q-5

maximum = max(ages)
print(maximum)

minum = min(ages)
print(minum)

# another way
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24,27]
# 1. maximum
maximum = 0
for age in ages:

    if age > maximum:
        maximum = age
    else:
        continue

print(f"maximum number: {maximum}")

# Q-6

compare_1 = minum - average
compare_2 = maximum - average
print(minum)
print(maximum)
print(average)

print(compare_1)
print(compare_2)
result = abs(compare_1 - compare_2)
print(result)


# additional challenge

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

#  1
middle_index = int((len(countries) -1) /2)
print(middle_index)

print(countries[middle_index])

# 2
first_half = countries[:middle_index]
first_half.append("One piece")
print(first_half)
print(len(first_half))

second_half = countries[middle_index:]
print(second_half)
print(len(second_half))

# 3

selected = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

china,russia,USA,*scandic_coutries = selected

print(china)
print(USA)
print(russia)
print(*scandic_coutries)



# -----------------------------#

