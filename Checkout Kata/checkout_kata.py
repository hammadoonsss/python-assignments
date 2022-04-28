def calculatePrice(string, items):

    items_count = {}
    for ch in string:
        if ch in items_count:
            items_count[ch] += 1
        else:
            items_count[ch] = 1
            
    sum = 0

    for key in items_count:
        if type(items[key]) == dict:
            rem = items_count[key] %  items[key]['count']
            div = items_count[key] // items[key]['count']
            sum += rem * items[key]['price'] + div * items[key]['discount_price']
            
        else:
            sum +=  items[key] * items_count[key]

    return sum


if __name__== '__main__':

    string = "AAA"
    items = {
        'A': {
                'price': 50,
                'count': 3,
                'discount_price': 130
            },
        'B': {
                'price': 30,
                'count': 2,
                'discount_price': 45
            },
        'C': 20,
        'D': 15
    }
    
    total_price = calculatePrice(string, items)
    print('Total Price: ', total_price)