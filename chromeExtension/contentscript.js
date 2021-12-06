console.log("Content Script Loaded from v-bucks")

chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  console.log("Message recieved in Content Script")
  if (request.message === 'nike') {
    console.log(`you made it to ${request.url} nice`)
    var div = document.createElement('div');
    var label = document.createElement('span');
    label.textContent = "Hello, samuel hi";
    div.appendChild(label);
    document.body.appendChild(div);
  }
  sendResponse({ result: "success" });
});