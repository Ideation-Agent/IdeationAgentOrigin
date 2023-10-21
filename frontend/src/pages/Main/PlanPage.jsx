import RoundBtn from "components/global/RoundBtn";
import {
  InnerOption,
  InnerOptionValue,
  InnerTitle,
} from "components/global/Texts";
import AllFullRow from "components/utils/AllFullRow";
import Block from "components/utils/Block";
import { LayerAlign } from "components/utils/WidgetUtils";

function PlanPage({ data }) {
  return (
    <>
      <InnerTitle>Finalized business plan for you</InnerTitle>

      <Block h={30} />
      <AllFullRow>
        <InnerOption>Business Plan:</InnerOption>
        <Block w={12} />
        <InnerOptionValue>{data["Business Plan"]}</InnerOptionValue>
      </AllFullRow>

      <Block h={40} />
      <AllFullRow>
        <InnerOption>Executive Summary:</InnerOption>
        <Block w={12} />
        <InnerOptionValue>{data["Executive Summary"]}</InnerOptionValue>
      </AllFullRow>
      <AllFullRow>
        <InnerOption>Mission:</InnerOption>
        <Block w={12} />
        <InnerOptionValue>{data["Mission"]}</InnerOptionValue>
      </AllFullRow>

      <Block h={40} />
      <AllFullRow>
        <InnerOption>Problem Statement:</InnerOption>
        <Block w={12} />
        <InnerOptionValue>{data["Problem Statement"]}</InnerOptionValue>
      </AllFullRow>

      <Block h={40} />
      <AllFullRow>
        <InnerOption>Solution:</InnerOption>
        <Block w={12} />
        <InnerOptionValue>{data["Solution"]}</InnerOptionValue>
      </AllFullRow>

      <Block h={40} />
      <AllFullRow>
        <InnerOption>Target Market:</InnerOption>
        <Block w={12} />
        <InnerOptionValue>{data["Target Market"]}</InnerOptionValue>
      </AllFullRow>

      <Block h={40} />
      <AllFullRow>
        <InnerOption>Revenue Model:</InnerOption>
        <Block w={12} />
        <InnerOptionValue>{data["Revenue Model"]}</InnerOptionValue>
      </AllFullRow>

      <Block h={40} />
      <AllFullRow>
        <InnerOption>Go-to-Market Strategy:</InnerOption>
        <Block w={12} />
        <InnerOptionValue>{data["Go-to-Market Strategy"]}</InnerOptionValue>
      </AllFullRow>

      <Block h={40} />
      <AllFullRow>
        <InnerOption>Competitive Analysis:</InnerOption>
        <Block w={12} />
        <InnerOptionValue>{data["Competitive Analysis"]}</InnerOptionValue>
      </AllFullRow>

      <Block h={40} />
      <AllFullRow>
        <InnerOption>Operational Plan:</InnerOption>
        <Block w={12} />
        <InnerOptionValue>{data["Operational Plan"]}</InnerOptionValue>
      </AllFullRow>

      <Block h={40} />
      <AllFullRow>
        <InnerOption>Conclusion:</InnerOption>
        <Block w={12} />
        <InnerOptionValue>{data["Conclusion"]}</InnerOptionValue>
      </AllFullRow>

      <Block h={40} />
      <AllFullRow main={LayerAlign.center}>
        <RoundBtn onClick={() => {
          // TODO: PDF 다운
        }}>Save</RoundBtn>
      </AllFullRow>
    </>
  );
}

export default PlanPage;
