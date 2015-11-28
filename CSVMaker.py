__author__ = 'chintanpanchamia'

import csv, cpancha

huntcsv = open('HuntHistory.csv', 'wb')
eb2csv = open('Eb2History.csv', 'wb')
carmichaelcsv = open('CarmichaelHistory.csv', 'wb')
ovalcsv = open('OvalHistory.csv', 'wb')
partycsv = open('PartyHistory.csv', 'wb')

huntwriter = csv.writer(huntcsv)
eb2writer = csv.writer(eb2csv)
carmichaelwriter = csv.writer(carmichaelcsv)
ovalwriter = csv.writer(ovalcsv)
partywriter = csv.writer(partycsv)

huntwriter.writerow(['Urgency', 'Relation', 'Noise Level', 'Action', 'Feedback'])
eb2writer.writerow(['Urgency', 'Relation', 'Noise Level', 'Action', 'Feedback'])
carmichaelwriter.writerow(['Urgency', 'Relation', 'Noise Level', 'Action', 'Feedback'])
ovalwriter.writerow(['Urgency', 'Relation', 'Noise Level', 'Action', 'Feedback'])
partywriter.writerow(['Urgency', 'Relation', 'Noise Level', 'Action', 'Feedback'])

huntcsv.close()
eb2csv.close()
carmichaelcsv.close()
ovalcsv.close()
partycsv.close()