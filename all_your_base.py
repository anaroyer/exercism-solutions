def rebase(input_base, digits, output_base):
    # STEP 0:
    if input_base < 2:
        raise ValueError('Input base must be at least 2')
    if len(digits) == 0:
        raise ValueError('You must provide at least one digit')
    if output_base < 2:
        raise ValueError('Output base must be at least 2')
    if all(index > 0 in digits) is False:
        raise ValueError('All digits must be positive')
    
    
    # STEP 1: 
    number = 0
    exponent = 0
    for digit in digits:
        exponent += 1
        multiply = digit * (input_base ** (len(digits) - exponent))
        number += multiply
    # STEP 2:
    closest_number = 0
    new_exponent = 0
    while closest_number <= number:
        new_exponent += 1
        closest_number = output_base ** new_exponent
    new_exponent -= 1
    closest_number = output_base ** new_exponent
   
   
    # STEP 3:
    symbols = range(output_base - 1)
    first_digit = number // closest_number
    remaining_of_number = number - (first_digit * (output_base ** new_exponent))
    new_digits = [first_digit]
    index = 1

    while remaining_of_number > 0:

        digit = remaining_of_number // (output_base ** (new_exponent - index))
        
        if digit in symbols:
            new_digits.append(digit)
            remaining_of_number = remaining_of_number - (digit * (output_base ** (new_exponent - index)))
            
        if digit not in symbols:
            digit = output_base - 1
            new_digits.append(digit)
            remaining_of_number = remaining_of_number - (digit * (output_base ** (new_exponent - index)))
        index += 1
            
            
    if len(new_digits) < (new_exponent + 1):
        while len(new_digits) != (new_exponent + 1):
            new_digits.append(0)
    return new_digits

# try using divmod() and replace the while with a for