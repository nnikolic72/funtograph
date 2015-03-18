/**
 * Created by n.nikolic on 3/18/2015.
 */

function like_callback(data) {
    var p_photo_id = data.p_photo_id;
    var id_name = '#likes_id_' + p_photo_id;
    var id_name_num = '#likes_num_' + p_photo_id;

    //alert(id_name)

    if (data.like_action_result == 'liked') {
        $(id_name).removeClass('glyphicon-heart-empty btn-default').addClass('glyphicon-heart btn-success');
        //alert('liked')
    }

    if (data.like_action_result == 'unliked') {
        $(id_name).removeClass('glyphicon-heart btn-success').addClass('glyphicon-heart-empty btn-default');
        //alert('unliked')
    }

    if (data.like_action_result == 'error') {
        $(id_name).addClass('btn-error');
    }

    $(id_name_num).html(data.no_of_likes)
}

function like(p_photo_id, static_url) {

    Dajaxice.interactions.like(like_callback, {'p_photo_id':p_photo_id});
}




function favorite_callback(data) {
    var p_photo_id = data.p_photo_id;
    var id_name = '#favorites_id_' + p_photo_id;
    var id_name_num = '#favorites_num_' + p_photo_id;

    //alert(id_name)

    if (data.favorite_action_result == 'favorited') {
        $(id_name).removeClass('glyphicon-star-empty btn-default').addClass('glyphicon-star btn-success');
        //alert('liked')
    }

    if (data.favorite_action_result == 'unfavorited') {
        $(id_name).removeClass('glyphicon-star btn-success').addClass('glyphicon-star-empty btn-default');
        //alert('unliked')
    }

    if (data.favorite_action_result == 'error') {
        $(id_name).addClass('btn-error');
    }

    $(id_name_num).html(data.no_of_favorites)
}


function favorite(p_photo_id, static_url) {

    Dajaxice.interactions.favorite(favorite_callback, {'p_photo_id':p_photo_id});
}


function send_comment_callback(data) {
    alert('Send comment callback');

}

function send_comment(p_photo_id) {

    var id_name = '#comment_form_' + p_photo_id;
    //alert(id_name);
    var data = $(id_name).serializeObject();
    //alert(data);
    Dajaxice.interactions.send_comment(send_comment_callback, {'p_photo_id':p_photo_id,
        'form': data});
}