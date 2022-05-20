import random
import art
import os
import time


def clear():
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')


def get_score(hand):
    score = 0

    for card in hand:
        rank = card.split(' ')[0]
        if rank == 'A':
            if score + 11 > 21:
                score += 1
            else:
                score += 11
        elif rank in 'JQK':
            score += 10
        else:
            score += int(rank)

    return score


def main():
    ranks = 'A 2 3 4 5 6 7 8 9 10 J Q K'
    deck = [
        f'{rank} of {suit}' for suit in 'CHDS' for rank in ranks.split(' ')
    ]
    random.shuffle(deck)

    while True:
        play = input('Play a game of Blackjack (\'y\' or \'n\'): ')
        clear()
        if play == 'n':
            break

        player_hand = []
        computer_hand = []

        for _ in range(2):
            player_hand.append(deck.pop(0))
            computer_hand.append(deck.pop(0))

        while True:
            print(art.logo)
            print(f'Your cards: {", ".join(player_hand)}')
            print(f'Computer\'s first card: {computer_hand[0]}')
            hit = input('Type \'y\' for another card, \'n\' to pass: ')
            if hit == 'y':
                player_hand.append(deck.pop(0))
            else:
                break

            current_score = get_score(player_hand)
            if current_score > 21:
                break

        while True:
            computer_score = get_score(computer_hand)
            if computer_score >= 21:
                break
            elif computer_score > 16:
                break
            else:
                computer_hand.append(deck.pop(0))

        player_score = get_score(player_hand)
        print(f'''
Your final hand: {", ".join(player_hand)} 
Final score: {player_score}
    ''')
        print(
            f'''Computer\'s final hand: {", ".join(computer_hand)}
Computer score: {computer_score}
    ''')

        if player_score > 21:
            print('YOU BUST! GAME OVER!')
        elif player_score == 21:
            print('YOU HIT 21! YOU WIN!')
        elif computer_score > 21:
            print('COMPUTER BUST! YOU WIN!')
        elif computer_score == 21:
            print('COMPUTER HIT 21! GAME OVER!')
        elif player_score > computer_score:
            print('YOU WIN!')
        else:
            print('YOU LOSE!')

        clear()


if __name__ == '__main__':
    main()
