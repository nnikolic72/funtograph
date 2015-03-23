/**
 * Created by n.nikolic on 3/23/2015.
 */

function photo_duel_vote_callback(data) {
    //alert('photo_duel_vote_callback');
    var p_photo_duel_id = data.p_photo_duel_id;
    var p_vote = data.p_vote;
    var action_result = data.action_result;
    var photo_duels_left = data.photo_duels_left


    var a_image_id = '#photo_a_' + p_photo_duel_id;
    var b_image_id = '#photo_b_' + p_photo_duel_id;
    var voting_panel_id = '#duel_id_' + p_photo_duel_id;

    if (action_result == 1) { // There was some action on duel
        if (p_vote == 'a') {
            $(b_image_id).fadeOut(600, function() { $(voting_panel_id).animate({
                opacity: 0.25,
                left: "+=50",
                height: "toggle"
            },900, function() { $(voting_panel_id).remove(); }) });
        }

        if (p_vote == 'b') {
            $(a_image_id).fadeOut(600, function() { $(voting_panel_id).animate({
                opacity: 0.25,
                left: "+=50",
                height: "toggle"
            },900, function() { $(voting_panel_id).remove(); }) });
        }

        if (p_vote == 'x') {
            $(voting_panel_id).animate({
                opacity: 0.25,
                left: "+=50",
                height: "toggle"
            },900, function() { $(voting_panel_id).remove(); });
        }

        if (photo_duels_left == 0) {
            // add text "No duels left"
            $('#dueling_panel').html('<p>No available photo duels to vote on Funtograph at this time. Want to start one?</p>')
        }

    }
}

function photo_duel_vote(p_photo_duel_id, p_vote) {
    //alert('Test');
    Dajaxice.duels.photo_duel_vote(photo_duel_vote_callback,
        {'p_photo_duel_id':p_photo_duel_id, 'p_vote':p_vote});
}