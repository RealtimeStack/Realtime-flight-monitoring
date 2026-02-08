const express = require("express");
const cors = require("cors");
const { Client } = require("@elastic/elasticsearch");

const app = express();
app.use(cors());

const es = new Client({
  node: "http://elastic:9200"   // container name
});

app.get("/alerts", async (req, res) => {
  try {
    const result = await es.search({
      index: "alerts",
      size: 0,
      aggs: {
        flights: {
          terms: {
            field: "flight_id.keyword",
            size: 10
          },
          aggs: {
            latest: {
              top_hits: {
                size: 1,
                sort: [
                  { "timestamp": { "order": "desc" } }
                ]
              }
            }
          }
        }
      }
    });

    const flights = result.aggregations.flights.buckets.map(b => {
      return b.latest.hits.hits[0]._source;
    });

    res.json(flights);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Elasticsearch error" });
  }
});

app.listen(8080, () => {
  console.log("Backend running on port 8080");
});

