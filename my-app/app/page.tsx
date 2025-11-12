export default async function Home() {
  const tempData = await fetch("http://127.0.0.1:8000/ev-incentives");
  const finalData = await tempData.json();



  const xAxis = finalData.map((temp) => temp.x);
  const yAxis = finalData.map((temp) => temp.y);

  return (
    <div>
      <h1 className="font-bold">WE ARE WINNING THIS!</h1>
      
    </div>
  );
}
 