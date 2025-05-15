from django.shortcuts import render, redirect
import random


def RollDice(request):

    default_num_sides = 6
    default_mode_name = 'single'
    default_num_dice = 1
    
    num_sides = request.session.get('current_num_sides', default_num_sides)
    current_mode_name = request.session.get('current_mode_name', default_mode_name)
    num_dice_input_value = request.session.get('current_num_dice_input_value', default_num_dice)
    roll_history = request.session.get('roll_history', [])

    current_roll_results = []
    current_roll_total = None

    num_dice_to_roll = 1 if current_mode_name == 'single' else num_dice_input_value

    if request.method == "POST":
        submitted_mode_button = request.POST.get("mode")
        if submitted_mode_button in ['single', 'multiple']:
            current_mode_name = submitted_mode_button
            request.session['current_mode_name'] = current_mode_name

            if current_mode_name == 'single':
                num_dice_to_roll = 1
                num_dice_input_value = 1
            

        if current_mode_name == 'multiple':
             try:
                 num_dice_input_value = int(request.POST.get("num_dice", request.session.get('current_num_dice_input_value', default_num_dice)))
    
                 if num_dice_input_value < 1:
                     num_dice_input_value = default_num_dice
             except (ValueError, TypeError):
                 num_dice_input_value = default_num_dice 

             num_dice_to_roll = num_dice_input_value
             request.session['current_num_dice_input_value'] = num_dice_input_value

        else: 
            num_dice_to_roll = 1
            num_dice_input_value = 1 

        num_sides_from_post = request.POST.get("num_sides")
        if num_sides_from_post is not None:
            try:
                posted_num_sides = int(num_sides_from_post)
                if posted_num_sides >= 2:
                    num_sides = posted_num_sides 
                    request.session['current_num_sides'] = num_sides
            except (ValueError, TypeError):
                 pass

        if 'mode' not in request.POST:
             if num_dice_to_roll < 1:
                 num_dice_to_roll = 1 
             current_roll_results = [random.randint(1, num_sides) for _ in range(num_dice_to_roll)]
             current_roll_total = sum(current_roll_results)

             roll_entry = {
                 'results': current_roll_results,
                 'total': current_roll_total,
                 'num_sides': num_sides, 
                 'num_dice': num_dice_to_roll, 
             }
             roll_history.append(roll_entry)
             request.session['roll_history'] = roll_history



    context = {
        "current_roll_results": current_roll_results,
        "current_roll_total": current_roll_total,
        "roll_history": roll_history,
        "current_mode_name": current_mode_name,
        "num_dice_value": num_dice_input_value,
        "num_sides_value": num_sides,
    }
    return render(request, "dice/index.html", context)


def clear_dice_history(request):
    if request.method == "POST":
        if 'roll_history' in request.session:
            del request.session['roll_history']
        return redirect('Dice:RollDice')
    else:
         return redirect('Dice:RollDice')