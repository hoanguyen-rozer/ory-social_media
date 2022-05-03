"use strict";

// Get comment form data and send to server, return result is comment data.
async function createComment(post_id) {

    // Get the comment form flowed by post id
    const form = document.querySelector(`.comment-form-${post_id}`);

    // Url add comment in the post
    const url = `/comment/add/${post_id}/`;

    const request = new Request(
        url,
        {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken,
            },
            mode: "same-origin",
            body: new FormData(form),
        }
    )

    try {
        let response = await fetch(request);
        const result = await response.json();
        return result;

    } catch (error) {
        console.log(error);
    }
}

const btns = document.querySelectorAll(".submit-add-comment");

// Add custom click event for each button.
for (const btn of btns) {
    btn.onclick = function (event) {
        event.preventDefault();
        const post_id = event.currentTarget.dataset['post'];
        const result = createComment(post_id);
        renderNewComment(result, post_id);
    }

}

// Function render new comment data to screen
function renderNewComment(comment, post_id) {
    const listComment = document.querySelector(`.list-comment-${post_id}`);
    const newComment = document.createElement('li');
    newComment.classList.add('comment');
    newComment.innerHTML = `
        <div class="user-img">
            <img src="${comment.user.avatar}" alt="userimg" class="img-45 radius-50">
        </div>
        <div class="comment__data">
            <h5>${comment.user.username}</h5>
            <p class="">${comment.content}</p>
            <div class="comment-activity">
                <a href="">like</a>
                <a href="">reply</a>
                <span> ${comment.created_at} </span>
            </div>
        </div>
    `
    listComment.insertBefore(newComment, listComment.firstElementChild);
}

async function expressFeeling(url) {

    // Url express feeling in the post

    const request = new Request(
        url,
        {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken,
            },
            mode: "same-origin",
        }
    )

    try {
        let response = await fetch(request);
        const result = await response.json();
        return result;

    } catch (error) {
        console.log(error);
    }
}

/* Process click event of 'like-link' anchors */

const likeAnchors = document.querySelectorAll(".like-link");

// Add custom click event for each like anchor.
for (const likeAnchor of likeAnchors) {
    likeAnchor.addEventListener('click', async function (event) {
            event.preventDefault();
            const url = event.currentTarget.getAttribute('href');
            const result = await expressFeeling(url);
            if (result.success === true) {
                changeIconLike(event);
            } else {
                console.log(result.message);
            }
        }
    )
}

// Change like icon when users click
function changeIconLike(event) {
    const icon = event.target;
    // Check icon whether have className, if icon thin then change it to solid icon and vice versa
    if (icon.classList.contains('bx-heart')) {
        icon.classList.remove('bx-heart');
        icon.classList.add('bxs-heart');
    } else {
        icon.classList.remove('bxs-heart');
        icon.classList.add('bx-heart');
    }
}



