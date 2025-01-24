def write_score():
    
    with open("high_score.txt", 'r') as f:
        
        content = f.read()
        
        print(content)
          
write_score()
        