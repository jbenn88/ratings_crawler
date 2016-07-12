movies = {
    Interstellar: 3.8,    
}


puts "What would you like to do? Choose from: add, update, display, or delete."
choice = gets.chomp

case choice
    when "add"
        puts "What is the movie's title?"
        title = gets.chomp.to_sym
        puts "What is your rating of this movie?"
        rating = gets.chomp.to_i
        
        if (movies[title.to_sym] == nil)
            movies[title] = rating;
        else
            puts "An entry already exists for this movie!"
        end
        
    when "update"
        puts "For which movie would you like to update the rating?"
        title = gets.chomp.to_sym
        puts "What is the updated rating?"
        rating = gets.chomp.to_i
        
        # Make sure a current entry exists to update, output error if not
        if (movies[title.to_sym] != nil)
            movies[title] = rating;
        else
            puts "There is no current entry for this movie! Try 'add' to create a                 new entry for this movie"
        end
        
    when "display"
        puts "Movies currently in database:"
        movies.each {|movie, rating|
            puts "#{movie}: #{rating}"
        
        }
    when "delete"
        puts "Which movie would you like to delete?"
        title = gets.chomp.to_sym
        
        if (movies[title] != nil)
            movies.delete(title)
        else
            puts "That movie does not currently exist in the database."
        end
    else
        puts "Error: not a valid operation. Please try again."
end


