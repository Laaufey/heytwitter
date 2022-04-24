
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

function toggleEditModal(){
  // alert();
  const modallogout = document.getElementById("editTweetModal").classList.toggle("hidden");

};

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

  if (!tweet_data.tweet_image){
    let tweet = `
    <form id="${tweet_data.tweet_id}" class="p-4 border-b border-slate-200">
    <div class="flex">
      <img class="flex-none w-12 h-12 rounded-full" src="/images/${tweet_data.user_img}" alt="">
      <div class="w-full pl-4">
        <ion-icon name="ellipsis-horizontal" class="absolute right-2 top-2 hover:bg-blue2/20 hover:text-blue1 transition ease-in-out duration-300 p-2 rounded-full"></ion-icon>
        <p class="font-thin text-xs"><a class="font-bold text-lg" href="/${tweet_data.user_name}">${tweet_data.user_first_name} ${tweet_data.user_last_name}</a> @${tweet_data.user_name}</p>
        <button class="text-sm text-gray-200" id="edit" class="edit">Edit</button>
        <div id="${tweet_data.tweet_id}" class="pt-2">
          ${_one("input", form).value}
        </div>
        <div class="flex gap-12 w-full mt-4 text-lg">
        <ion-icon class="ml-auto hover:text-blue1 cursor-pointer" name="trash-outline" onclick="deleteTweet(${tweet_data.tweet_id})"></ion-icon>
        <ion-icon class="hover:text-blue1 cursor-pointer" name="chatbox-ellipses-outline"></ion-icon>
        <ion-icon class="hover:text-blue1 cursor-pointer" name="heart-outline"></ion-icon>
        <ion-icon class="hover:text-blue1 cursor-pointer" name="sync-outline"></ion-icon>                  
        <ion-icon class="hover:text-blue1 cursor-pointer" name="share-outline"></ion-icon>
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
      <div class="w-full pl-4">
        <ion-icon name="ellipsis-horizontal" class="absolute right-2 top-2 hover:bg-blue2/20 hover:text-blue1 transition ease-in-out duration-300 p-2 rounded-full"></ion-icon>
        <p class="font-thin text-xs"><a class="font-bold text-lg" href="/${tweet_data.user_name}">${tweet_data.user_first_name} ${tweet_data.user_last_name}</a> @${tweet_data.user_name}</p>
        <button class="text-sm text-gray-200" id="edit" class="edit">Edit</button>
        <div id="${tweet_data.tweet_id}" class="pt-2">
          ${_one("input", form).value}
        </div>
        <img
        class="mt-2 w-full object-cover h-80"
        src="/images/${tweet_data.tweet_image}"
        />
        <div class="flex gap-12 w-full mt-4 text-lg">
        <ion-icon class="ml-auto hover:text-blue1 cursor-pointer" name="trash-outline" onclick="deleteTweet(${tweet_data.tweet_id})"></ion-icon>
        <ion-icon class="hover:text-blue1 cursor-pointer" name="chatbox-ellipses-outline"></ion-icon>
        <ion-icon class="hover:text-blue1 cursor-pointer" name="heart-outline"></ion-icon>
        <ion-icon class="hover:text-blue1 cursor-pointer" name="sync-outline"></ion-icon>                  
        <ion-icon class="hover:text-blue1 cursor-pointer" name="share-outline"></ion-icon>
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

const btnEditTweet = document.getElementById("edit")
btnEditTweet.addEventListener("click", editTweet);
const editModal = document.getElementById("editTweetModal")
console.log(editModal)




async function editTweet(tweet_id){
  event.preventDefault()
  console.log({tweet_id})
  const connection = await fetch(`/tweets/${tweet_id}`, {
    
    method: "PUT",
    body: new FormData(document.getElementById("edit-tweet")),
  })
  console.log(connection)
  const response = await connection

  if (!response.ok) return alert("Can't edit the tweet")
  toggleEditModal()
}

async function deleteTweet(tweet_id){
  // Connect to the api and delete it from the "database"
  const connection = await fetch(`/tweets/${tweet_id}`, {
    method : "DELETE"
  })
  if( ! connection.ok ){
    alert("uppps... try again")
    return
  }
  console.log(document.querySelector(`[id='${tweet_id}']`))
  document.querySelector(`[id='${tweet_id}']`).remove()
}



