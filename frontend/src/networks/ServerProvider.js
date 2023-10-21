import axios from "axios";

const baseUrl = "https://localhost:8010";

const api = axios.create({
  baseURL: baseUrl,
  headers: {
    "Content-Type": "application/json",
  },
});

class ServerProvider {
  async checkBio({ url }) {
    try {
      const response = await api.post("", {
        linkedin_url: url,
      });

      return response.data;
    } catch (e) {
      console.log(e);
      // return false;
      return {
        profileName: "string",
        linkedin_summary: "string",
      };
    }
  }

  async genInitIdea({ sum, interests }) {
    try {
      const reponse = await api.post("", {
        linkedin_summary: sum,
        interests,
      });

      return reponse.data;
    } catch (e) {
      console.log(e);
      // return false;
      return {
        ideas: [
          {
            service_name: "AI Resume Assistant",
            problem:
              "Current resume writing processes are time-consuming and often result in poorly formatted or ineffective resumes.",
            solution:
              "- Develop an AI-powered assistant that can analyze a user's career history and provide personalized suggestions for",
          },
          {
            service_name: "AI Personal Stylist",
            problem:
              "Many individuals struggle with fashion choices, lack knowledge about current trends, or face difficulties in styling",
            solution:
              "- Create an AI-powered personal stylist that analyzes a user's body type, preferences, and current wardrobe.\n- Prov",
          },
          {
            service_name: "AI Language Tutor",
            problem:
              "Learning a new language can be challenging without personalized guidance and regular practice.",
            solution:
              "- Develop an AI-based language tutor that offers personalized language lessons to users.\n- Use natural language pro",
          },
          {
            service_name: "AI Health Coach",
            problem:
              "Maintaining a healthy lifestyle can be overwhelming, and individuals often struggle with setting and achieving health",
            solution:
              "- Create an AI-powered health coach that provides personalized recommendations based on the user's health data, goal",
          },
          {
            service_name: "AI Travel Planner",
            problem:
              "Planning a trip can be time-consuming and overwhelming, especially when there are multiple destinations and preferenc",
            solution:
              "- Develop an AI travel planner that helps users with itinerary creation, destination recommendations, and travel boo",
          },
        ],
      };
    }
  }

  async dialog({ log, input, speaker }) {
    try {
      const response = await api.post("", {
        log,
        human_input: input,
        speaker_list: speaker,
      });

      return response.data;
    } catch (e) {
      console.log(e);
      return false;
    }
  }

  async conclusion({ log }) {
    try {
      const response = await api.post("", {
        log,
      });

      return response.data;
    } catch (e) {
      console.log(e);
      return false;
    }
  }
}

export default ServerProvider;
