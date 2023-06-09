#!/usr/bin/env python3

import click

@click.group() # 최상위 그룹 만들기
def cli():
    pass

@click.group(help='Ship related commands') # ships 명령을 보유할 그룹 만들기
def ships():
    pass

cli.add_command(ships) # 최상위 그룹 명령 추가

@ships.command(help='Sail a ship') # 명령어 추가
def sail():
    ship_name = 'Your ship'
    print(f"{ship_name} is setting sail")

@ships.command(help='List all of the ships')
def list_ships():
    ships = ['John B', 'Yankee Clipper', 'Pequod']
    print(f"Ships: {','.join(ships)}")

@cli.command(help='Talk to a sailor') # 명령어 추가
@click.option('--greeting', default='Ahoy there', help='Greeting for sailor')
@click.argument('name')
def sailors(greeting, name):
    message = f'{greeting} {name}'
    print(message)

if __name__ == '__main__':
    cli() # 최상위ㅣ 그룹 호출
