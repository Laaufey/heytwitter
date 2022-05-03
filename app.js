
function _all(q, e=document){return e.querySelectorAll(q)}
function _one(q, e=document){return e.querySelector(q)}

function returnFalse(){
  if (document.myForm.myText.value == '')
      return false;
      // When it returns false - your form will not submit and will not redirect too
  else
      return true;
   // When it returns true - your form will submit and will redirect
// (actually it's a part of submit) id you have mentioned in action
};

// const queryString = window.location.search
// if (queryString) {
//     const urlParams = new URLSearchParams(queryString)
//     if (urlParams.get("error")){
//         document.querySelector("#signUpModal").classList.toggle("hidden")
//     }
// }
function toggleSignUpModal(){

    // _one("#signUpModal").classList.toggle("hidden")
    const signupmodal = document.getElementById("signUpModal").classList.toggle("hidden");
  }

function toggleSignInModal(){
  const loginmodal = document.getElementById("loginModal").classList.toggle("hidden");
}

function showTweetModal(){
  // alert();
  const modal = document.getElementById("tweetModal").classList.remove("hidden");

};

function hideTweetModal(){
  // alert();
  const modal = document.getElementById("tweetModal").classList.add("hidden");

};

function toggleTweetModal(){
  // alert();
  const modal = document.getElementById("tweetModal").classList.toggle("hidden");
};

function toggleModal(){
  // alert();
  const modallogout = document.getElementById("logoutModal").classList.toggle("hidden");
  
};

function toggleEditModal(modal){
  // alert();
  // const modalupdate = document.getElementById("update_tweet_modal").classList.toggle("hidden");
  _one(modal).classList.toggle("hidden")
}
function openEditModal(){
  // alert();
  const modalupdate = document.getElementById("update_tweet_modal").classList.toggle("hidden");
  // _one(modal).classList.toggle("hidden")

}
function updateModalContent(){
  tweetId = event.target.dataset.id
  console.log(event)
  const modal = document.getElementById("update_tweet_modal")
  modal.querySelector("form").dataset.id = tweetId
  console.log(tweetId)
}

function editProfileModal(){
  // alert();
  const editProfile = document.getElementById("edit_profile_modal").classList.toggle("hidden");
  // _one(modal).classList.toggle("hidden")
}

async function sendTweet(){
  const form = event.target
  // Get the button, set the data-await, and disable it
  const button = _one("button[type='submit']", form)
  // console.log(button)
  // button.innerText = button.dataset.await
  // button.innerText = button.getAttribute("data-await")
  // button.disabled = true

  const connection = await fetch("/post_tweet", {
    method : "POST",
    body : new FormData(form)
  })

  // button.disabled = false
  // button.innerText = button.dataset.default

  if( ! connection.ok ){
    alert("error")
    return
  }
  const tweet_data = await connection.json() // tweet id will be here
  console.log("Tweet")
  console.log(tweet_data)
  console.log(connection)
  console.log("Tweet id")
  console.log(tweet_data.tweet_id)
  console.log("fk-user-id")
  console.log(tweet_data.fk_user_id)



  if (!tweet_data.tweet_image){
    let tweet = `
    <form id="${tweet_data.tweet_id}" class="p-4 border-b border-slate-200">
    <div class="flex">
      <img class="flex-none w-12 h-12 rounded-full" src="/images/${tweet_data.user_img}" alt="">
      <div class="w-full relative pl-4">
      <button class="absolute right-2" onclick="${openDropDown()}"><ion-icon id="${tweet_data.tweet_id}" name="ellipsis-horizontal" class="absolute right-2 top-2 hover:bg-blue2/20 hover:text-blue1 cursor-pointer transition ease-in-out duration-300 p-2 rounded-full"></ion-icon></button>
      <div id="drop-down-${tweet_data.tweet_id}" class="drop-down absolute right-10 top-2 hidden z-20 bg-white divide-y  rounded shadow w-40 ">
      <ul class="py-1 text-sm" aria-labelledby="dropdownLeftStartButton">
      <li>
      <a href="#" class="block px-4 py-2 hover:bg-gray-100  text-blue1">Follow @${tweet_data.user_name}</a>
      </li>
      <li>
      <a href="#" class="block px-4 py-2 hover:bg-gray-100  text-blue1">Report</a>
      </li>
      </ul>
      </div>  
      <p class="font-thin text-xs"><a class="font-bold text-lg" href="/${tweet_data.user_name}">${tweet_data.user_first_name} ${tweet_data.user_last_name}</a> @${tweet_data.user_name}</p>
        <div id="${tweet_data.tweet_id}" class="pt-2">
          ${_one("input", form).value}
        </div>
        <div class="flex gap-12 w-full mt-4 text-lg">
        <ion-icon class="ml-auto p-2 hover:text-blue1 cursor-pointer" name="trash-outline" onclick="deleteTweet('${tweet_data.tweet_id}')"></ion-icon>
        <ion-icon class="p-2 hover:text-blue1 cursor-pointer" name="chatbox-ellipses-outline"></ion-icon>
        <ion-icon class="p-2 hover:text-blue1 cursor-pointer" name="heart-outline"></ion-icon>        
        <ion-icon class="p-2 hover:text-blue1 cursor-pointer" name="share-outline"></ion-icon>
      </div>
      </div>
    </div>
  </form> 
  `
  _one("input", form).value = ""  

  _one("#tweets").insertAdjacentHTML("afterbegin", tweet)
  } else {
    let tweet = `
    <form id="${tweet_data.tweet_id}" class="p-4 border-b border-slate-200">
    <div class="flex">
      <img class="flex-none w-12 h-12 rounded-full" src="/images/${tweet_data.user_img}" alt="">
      <div class="w-full relative pl-4">  
      <button class="absolute right-2" onclick="${openDropDown()}"><ion-icon id="${tweet_data.tweet_id}" name="ellipsis-horizontal" class="absolute right-2 top-2 hover:bg-blue2/20 hover:text-blue1 cursor-pointer transition ease-in-out duration-300 p-2 rounded-full"></ion-icon></button>
      <div id="drop-down-${tweet_data.tweet_id}" class="drop-down absolute right-10 top-2 hidden z-20 bg-white divide-y  rounded shadow w-40 ">
      <ul class="py-1 text-sm" aria-labelledby="dropdownLeftStartButton">
      <li>
      <a href="#" class="block px-4 py-2 hover:bg-gray-100  text-blue1">Follow @${tweet_data.user_name}</a>
      </li>
      <li>
      <a href="#" class="block px-4 py-2 hover:bg-gray-100  text-blue1">Report</a>
      </li>
      </ul>
      </div>
      <p class="font-thin text-xs"><a class="font-bold text-lg" href="/${tweet_data.user_name}">${tweet_data.user_first_name} ${tweet_data.user_last_name}</a> @${tweet_data.user_name}</p>
        <div id="${tweet_data.tweet_id}" class="pt-2">
          ${_one("input", form).value}
        </div>
        <img
        class="mt-2 w-full object-cover h-80"
        src="/images/${tweet_data.tweet_image}"
        />
        <div class="flex gap-12 w-full mt-4 text-lg">
        <ion-icon class="ml-auto p-2 hover:text-blue1 cursor-pointer" name="trash-outline" onclick="deleteTweet('${tweet_data.tweet_id}')"></ion-icon>
        <ion-icon class="p-2 hover:text-blue1 cursor-pointer" name="chatbox-ellipses-outline"></ion-icon>
        <ion-icon class="p-2 hover:text-blue1 cursor-pointer" name="heart-outline"></ion-icon>                  
        <ion-icon class="p-2 hover:text-blue1 cursor-pointer" name="share-outline"></ion-icon>
      </div>
      </div>
    </div>
  </form> 
  `
  _one("input", form).value = ""  

  _one("#tweets").insertAdjacentHTML("afterbegin", tweet)
  }
  // Success

  
}

function updateImageContent(){
  userId = event.target.dataset.id
  console.log(event)
  const modal = document.getElementById("update_tweet_modal")
  modal.querySelector("form").dataset.id = tweetId
  console.log(tweetId)
}

async function editProfilePicture(){
  const form = event.target
  console.log(form)
  const id = form.id
  console.log(id)
  // console.log(id)
  const connection = await fetch(`/users/${id}`, {
    method: "PUT",
    body: new FormData(form)
  })
  if ( ! connection.ok ) {
    alert("Can't edit the photo")
    return
  }
  const image = await connection.text()
  document.querySelector(`[id=${id}]`).querySelector("[data-img]").textContent = image
}

async function updateTweet(){
  const form = event.target
  const id = form.dataset.id
  console.log(form)
  const connection = await fetch(`/tweets/${id}`, {
    method: "PUT",
    body: new FormData(form)
  })
  if ( ! connection.ok ) {
    alert("Can't edit the tweet")
    return
  }
  const tweetText = await connection.text()
  document.querySelector(`[id=${id}]`).querySelector("[data-text]").textContent = tweetText
}

async function deleteTweet(tweet_id, user_name){
  // Connect to the api and delete it from the "database"
  const connection = await fetch(`/tweets/${tweet_id}`, {
    method : "DELETE"
  })
  if( ! connection.ok ){
    alert("uppps... try again")
    return
  }
  const tweet_data = await connection.json()
  user_name = tweet_data.user_name
  console.log(tweet_data)
  console.log(tweet_data.username)

  // console.log(document.querySelector(`[id='${tweet_id}']`))
  document.querySelector(`[id='${tweet_id}']`).remove()
}

async function likeTweet(tweet_id){
  const connection = await fetch(`/tweets/${tweet_id}/like`, {
    method : "POST"
  })
  if( ! connection.ok ){
    alert("uppps... try again")
    return
  }
  const likeBtn = document.getElementById("like-btn-" + tweet_id)
  likeBtn.classList.add("hidden")
  const unlikeBtn = document.getElementById("unlike-btn-" + tweet_id)
  unlikeBtn.classList.remove("hidden")

  let count = document.getElementById("count-" + tweet_id).innerHTML
  count++
  document.getElementById("count-" + tweet_id).innerHTML = count
  document.getElementById("count-" + tweet_id).classList.remove("hidden")
}

async function unlikeTweet(tweet_id){
  console.log("HELLO DELETE")
  const connection = await fetch(`/tweets/${tweet_id}/unlike`, {
    method : "DELETE"
  })
  if( ! connection.ok ){
    alert("uppps... try again")
    return
  }
  const likeBtn = document.getElementById("like-btn-" + tweet_id)
  likeBtn.classList.remove("hidden")
  const unlikeBtn = document.getElementById("unlike-btn-" + tweet_id)
  unlikeBtn.classList.add("hidden")

  let count = document.getElementById("count-" + tweet_id).innerHTML
  count -= 1
  document.getElementById("count-" + tweet_id).innerHTML = count
  if (count == 0) {
    document.getElementById("count-" + tweet_id).classList.add("hidden")
  }
}

async function openDropDown(){
  const btn = event.target
  const id = btn.id
  console.log(btn)
  console.log(id)

  const dd = document.getElementById("drop-down-" + id)
  dd.classList.toggle("hidden")
}


