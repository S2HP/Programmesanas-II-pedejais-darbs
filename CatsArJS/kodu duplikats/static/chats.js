const ATJAUNOT = 1000;


async function sutitZinu(){
  let zina = document.getElementById("zinasVieta").value;
  document.getElementById("zinasVieta").value = "";
  let lietotajvards = document.getElementById("lietotajvards").value;
  const atbilde = await fetch('/sutit',{
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({"zina": zina,"user":lietotajvards})
  },)
  console.log(await atbilde.json());
}


async function ieladetChatu(){
  const atbilde = await fetch('/lasit');
  const chataSaturs = await atbilde.json();
  raditChatu(chataSaturs);
  await new Promise(resolve => setTimeout(resolve, ATJAUNOT));
  await ieladetChatu();
}

function raditChatu(saturs){
  let vieta = document.getElementById("chats");
  let jaunaRinda = "<br>"
  let chats = ""
  for (rinda of saturs){
    chats += rinda + jaunaRinda
  }
  vieta.innerHTML = chats;
}