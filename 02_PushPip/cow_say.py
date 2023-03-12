import cowsay
import argparse
import sys


parser = argparse.ArgumentParser(prog="cow_say",
                                 description="Works like python-cowsay, but with -l support",
                                 epilog='End of description. Now its time to try it:)')
parser.add_argument('message',
                    nargs='?',
                    default='',
                    help='message you want a cow to say')
parser.add_argument("-e", "--eye_string",
                    dest="eyes",
                    default=cowsay.Option.eyes,
                    help='choose your cows eyes')
parser.add_argument("-f", "--file")
parser.add_argument("-l",
                    action="store_true",
                    help='view list of available animals')
parser.add_argument("-n",
                    action="store_false",
                    dest="wrap_text",
                    help='choose in case of arbitrary message')
parser.add_argument("-T", "--tongue_string",
                    dest="tongue",
                    default=cowsay.Option.tongue,
                    help='choose your cows tongue')
parser.add_argument("-W", "--column",
                    dest="width",
                    default=40,
                    type=int,
                    help='choose your cows width')
parser.add_argument("-bdgpstwy", dest="preset")
args = parser.parse_args()

if args.l:
    print(cowsay.list_cows())
else:
    print(cowsay.cowsay(args.message,
                        preset=args.preset,
                        eyes=args.eyes,
                        tongue=args.tongue,
                        width=args.width,
                        wrap_text=args.wrap_text,
                        cowfile=args.file))

