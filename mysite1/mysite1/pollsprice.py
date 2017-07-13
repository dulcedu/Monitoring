from django.core.management.base import BaseCommand, CommandError
from models import bitcoinprice
from exchanges.coindesk import CoinDesk

class Command(BaseCommand):
    help = 'Script to pull prices'


    def handle(self, *args, **options):

        HDCoinDesk = get_historical_data_as_list(start'2017-06-29', end=None)

        print HDCoinDesk
