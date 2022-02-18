#Display seconds as Hours/Mins/Seonds
total_secs = int(input('Enter time in seconds:'))
hours = total_secs//3600
seconds_remaining = total_secs%3600
minutes = seconds_remaining//60
seconds = seconds_remaining%60
print('Hours/Mins/Seconds:',hours,'/',minutes,'/',seconds)
