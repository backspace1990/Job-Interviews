candidates = [
 {"name": "Vasya",  "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores":0},
 {"name": "Fedya",  "scores": {"math": 33, "russian_language": 85, "computer_science": 42},  "extra_scores":2},
 {"name": "Petya",  "scores": {"math": 92, "russian_language": 33, "computer_science": 34},  "extra_scores":1},
 {"name": "Vasya1",  "scores": {"math": 30, "russian_language": 62, "computer_science": 48}, "extra_scores":0},
 {"name": "Fedya1",  "scores": {"math": 33, "russian_language":63, "computer_science": 42},  "extra_scores":2},
 {"name": "Vasya2",  "scores": {"math": 36, "russian_language": 64, "computer_science": 70}, "extra_scores":0},
 {"name": "Fedya2",  "scores": {"math": 38, "russian_language": 65, "computer_science": 42},  "extra_scores":1},
 {"name": "Vasya3",  "scores": {"math": 40, "russian_language": 66, "computer_science": 48}, "extra_scores":0},
 {"name": "Fedya3",  "scores": {"math": 41, "russian_language": 67, "computer_science": 72},  "extra_scores":2},
 {"name": "Vasya4",  "scores": {"math": 42, "russian_language": 68, "computer_science": 68}, "extra_scores":0},
 {"name": "Fedya4",  "scores": {"math": 43, "russian_language": 69, "computer_science": 42},  "extra_scores":2},
 {"name": "Vasya5",  "scores": {"math": 44, "russian_language": 70, "computer_science": 48}, "extra_scores":0},
 {"name": "Fedya5",  "scores": {"math": 45, "russian_language": 71, "computer_science": 42},  "extra_scores":2},
 {"name": "Vasya6",  "scores": {"math": 46, "russian_language": 72, "computer_science": 48}, "extra_scores":0},
 {"name": "Fedya6",  "scores": {"math": 47, "russian_language": 73, "computer_science": 90},  "extra_scores":1},
 {"name": "Vasya7",  "scores": {"math": 48, "russian_language": 74, "computer_science": 48}, "extra_scores":0},
 {"name": "Fedya7",  "scores": {"math": 49, "russian_language": 75, "computer_science": 42},  "extra_scores":1},
 {"name": "Vasya8",  "scores": {"math": 50, "russian_language": 76, "computer_science": 87}, "extra_scores":0},
 {"name": "Fedya8",  "scores": {"math": 51, "russian_language": 77, "computer_science": 90},  "extra_scores":2},
 {"name": "Vasya9",  "scores": {"math": 52, "russian_language": 78, "computer_science": 48}, "extra_scores":0},
 {"name": "Fedya9",  "scores": {"math": 53, "russian_language": 79, "computer_science": 56},  "extra_scores":1},
 {"name": "Vasya11",  "scores": {"math": 54, "russian_language": 80, "computer_science": 48}, "extra_scores":0},
 {"name": "Fedya11",  "scores": {"math": 55, "russian_language": 81, "computer_science": 42},  "extra_scores":2},
 {"name": "Vasya12",  "scores": {"math": 56, "russian_language": 82, "computer_science": 34}, "extra_scores":1},
 {"name": "Fedya12",  "scores": {"math": 57, "russian_language": 83, "computer_science": 30},  "extra_scores":0},
 {"name": "Vasya13",  "scores": {"math": 58, "russian_language": 84, "computer_science": 33}, "extra_scores":1},
 {"name": "Fedya13",  "scores": {"math": 59, "russian_language": 85, "computer_science": 33},  "extra_scores":2}
]

def fin_top_20(canditdates):
    for candidat in candidates:
        course_scores = sum(candidat["scores"].values())
        scr_extr = candidat['extra_scores']
        candidat['scr_sum'] = course_scores + scr_extr

    candidates1 = sorted(candidates, key=lambda k : k['scr_sum'], reverse=True)
    winner_candidates=[]
    i = 0
    for W_candidates in candidates1:
        if i == 20:
            break
        winner_candidates.append(W_candidates['name'])
        i += 1
    
    return winner_candidates



def main():
    print(fin_top_20(canditdates=candidates))

if __name__ == '__main__':
    main()