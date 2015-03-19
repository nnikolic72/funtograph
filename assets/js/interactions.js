/**
 * Created by n.nikolic on 3/18/2015.
 */

function like_callback(data) {
    //alert(data.like_action_result);
    var p_photo_id = data.p_photo_id;
    var id_name_likes = '#likes_id_' + p_photo_id;
    var id_name_unlikes = '#unlikes_id_' + p_photo_id;
    var id_name_num_likes = '#likes_num_' + p_photo_id;
    var id_name_num_dislikes = '#dislikes_num_' + p_photo_id;

    //alert(id_name)
    $(id_name_likes).addClass('btn-default').removeClass('btn-success')
    $(id_name_unlikes).addClass('btn-default').removeClass('btn-danger')

    if (data.like_action_result == 'like_button-pressed') {
        $(id_name_likes).addClass('btn-success');
        //alert('liked')
    }
   if (data.like_action_result == 'unlike_button-pressed') {
        $(id_name_unlikes).addClass('btn-danger');
        //alert('liked')
    }


    if (data.like_action_result == 'error') {
        $(id_name_likes).addClass('btn-warning');
        $(id_name_unlikes).addClass('btn-warning');
    }

    $(id_name_num_likes).html(data.no_of_likes);
    $(id_name_num_dislikes).html(data.no_of_dislikes);
}

function like(p_photo_id, static_url, pressed_button) {
    //alert('in like');
    Dajaxice.interactions.like(like_callback,
        {   'p_photo_id':p_photo_id,
            'p_pressed_button': pressed_button

        }
    );
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

    $(id_name_num).html(data.no_of_favorites);
}


function favorite(p_photo_id, static_url) {

    Dajaxice.interactions.favorite(favorite_callback, {'p_photo_id':p_photo_id});
}


function send_comment_callback(data) {
    //alert('Send comment callback');
    var p_photo_id = data.p_photo_id;
    var id_name_num = '#comments_num_' + p_photo_id;

    alert(id_name_num);

    $(id_name_num).html(data.no_of_comments);

}

function send_comment(p_photo_id) {

    var id_name = '#comment_form_' + p_photo_id;
    //alert(id_name);
    var data = $(id_name).serializeObject();
    //alert(data);
    Dajaxice.interactions.send_comment(send_comment_callback, {'p_photo_id':p_photo_id,
        'form': data});
}