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
    var p_is_first = data.p_is_first;
    var new_comment_id = data.new_comment_id;
    var id_name_num = '#comments_num_' + p_photo_id;
    var id_comments_text= '#comment_photo_id_' + p_photo_id;
    var logged_photographer_name = data.logged_photographer_name;
    var comment_text = data.comment_text;

    var glyph_text = '';

    if (p_is_first == 1) {
        $(id_comments_text).html(comment_text);
    }
    else
    {
        var new_comment_to_append = '';
        new_comment_to_append += '<div id="comment_id_' + new_comment_id + '">';
        new_comment_to_append += '<p>';
        new_comment_to_append += '<button class="btn btn-xs glyphicon glyphicon-trash btn-default" ';
        new_comment_to_append += ' id="comment_id_delete_comment_' + new_comment_id + '" ';
        new_comment_to_append += ' onclick="delete_comment(' + p_photo_id + ', ' + new_comment_id + ' );">';
        new_comment_to_append += '</button>';
        new_comment_to_append += '<br>';
        new_comment_to_append += '<strong class="text-info">' + logged_photographer_name + '</strong>: ' + comment_text + '&nbsp;';
        new_comment_to_append += '</p>';
        new_comment_to_append += '<hr>';
        new_comment_to_append += '</div>';

        //alert(new_comment_to_append);
        $(id_comments_text).append(new_comment_to_append)

        //$(id_comments_text).append('h1').html('Proba');
    }

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


function delete_comment_callback(data) {
    //alert('Delete comment callback' + data);

    var p_comment_id = data.p_comment_id;
    var action_result = data.action_result;
    var no_of_comments = data.no_of_comments;

    var id_name = '#comment_id_' + p_comment_id;

    //$(id_name).remove();
    //alert('Removed:' + id_name);
    $(id_name).fadeOut(600, function() { $(id_name).remove(); });

}

function delete_comment(p_comment_id) {
    //alert('Delete comment clicked ' + p_comment_id);
    Dajaxice.interactions.delete_comment(delete_comment_callback, {'p_comment_id':p_comment_id});
}

function like_comment_callback(data) {
    //alert('Like comment callback' + data);
    var p_comment_id = data.p_comment_id;
    var action_result = data.action_result;
    var no_of_not_liked_comments = data.no_of_not_liked_comments;
    var id_name = '#comment_id_thumbs_up_' + p_comment_id;

    if (action_result == 'unliked') {
        $(id_name).removeClass('btn-info').addClass('btn-default');
    }

    if (action_result == 'liked') {
        $(id_name).removeClass('btn-default').addClass('btn-info');
    }

}

function like_comment(p_comment_id) {

    Dajaxice.interactions.like_comment(like_comment_callback, {'p_comment_id':p_comment_id});
}


function reply_comment(p_comment_id) {
    // open up comment form
    var id_name = '#comment_reply_div_' + p_comment_id;

    if ($(id_name).is(":hidden")) {
        $(id_name).show(400);
    } else
    {
       $(id_name).hide(400);
    }

}