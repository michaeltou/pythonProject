#!/usr/bin/env python3


import argparse

def main():
    parser = argparse.ArgumentParser(description='This is a test program.')
    parser.add_argument('outfile')
    parser.add_argument('--host', default='localhost')
    parser.add_argument('--port', default='3306', type=int)

    parser.add_argument('-u', '--user', required=True)
    parser.add_argument('-p', '--password', required=True)
    parser.add_argument('--database', required=True)

    # gz参数不跟参数值，因此指定action='store_true'，意思是出现-gz表示True:
    parser.add_argument('-gz', '--gzcompress', action='store_true', required=False, help='Compress backup files by gz.')

    parser.add_argument('outfile2')

    args = parser.parse_args()
    # 打印参数:
    print('parsed args:')
    print(f'outfile = {args.outfile}')
    print(f'outfile2 = {args.outfile2}')
    print(f'host = {args.host}')
    print(f'port = {args.port}')
    print(f'user = {args.user}')
    print(f'password = {args.password}')
    print(f'database = {args.database}')
    print(f'gzcompress = {args.gzcompress}')

if __name__ == '__main__':
    main()