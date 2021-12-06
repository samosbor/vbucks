let color = '#3aa757';

chrome.runtime.onInstalled.addListener(() => {
  chrome.storage.sync.set({ color });
  console.log('Default background color set to %cgreen', `color: ${color}`);
});

chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
  if (changeInfo.url) {
    if (changeInfo.url === "https://www.nike.com/"){
      setTimeout(() => chrome.tabs.sendMessage( tabId, {message: 'nike', url: changeInfo.url}), 1000) // i think the site has to be completely loaded or somehting.
      console.log("Sent the message to content script")
    }
  }
})