TIME_STRUCTURE = {
    'year' : 1,#n
    'month' : [1, 2, 3, 4],#[1..4] * n
    'day' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
             30, 31, 32],#[1..32]
    'season' : ['V', 'O', 'I', 'P']#cat
    'month_day' : {
        1 : {
            'days' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                      28, 29, 30, 31, 32],
            'weeks' : [11, 10, 11]
        },
        2 : {
            'days': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                     28, 29, 30, 31],
            'weeks': [10, 11, 10]
        },
        3 : {
            'days': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                     28, 29, 30, 32],
            'weeks': [11, 10, 11]
        },
        4 : {
            'days': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                     28, 29, 30, 31],
            'weeks': [10, 11, 10]
        }
    }
}

START_TIME = {
    'year' : 1,
    'season' : {
        'I' : ['diamonds', 'cups'],
        'V' : ['clubs', 'spades']
    },
    'month' : 1,
    'day': 1,

}