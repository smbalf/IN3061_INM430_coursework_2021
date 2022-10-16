import pandas as pd


ticket_df = pd.read_excel('ticketPrices.xlsx')
ticket_df.to_csv (r'ticketPrices.csv', index = None, header=True)

passenger_csv = pd.read_csv('passengerData.csv')
ticket_csv = pd.read_csv('ticketPrices.csv')

passenger_df = pd.DataFrame(passenger_csv)
ticket_df = pd.DataFrame(ticket_csv)

merged_df = (pd.merge(passenger_df, ticket_df, on='TicketType'))

max_age = merged_df['Age'].max() # 80

oldest_passenger = merged_df[(merged_df.Age == max_age)]
oldest_passenger_name = oldest_passenger.Name # Barkworth, Mr. Algernon Henry Wilson

# merged_df.plot.scatter(5, 7)


"""mean_fare = round((sum(merged_df.Fare))/890, 0)

sum_age = 0

for age in merged_df.Age:
    try:
        sum_age += int(age)
    except ValueError:
        pass

mean_age = round(sum_age / 890, 0)

print(mean_fare)
print(mean_age)
"""
