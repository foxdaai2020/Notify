<template>
  <div>
    <title-bar serviceListFilter="true">Service List</title-bar>
    <div class="d-flex align-center table-action">
      <v-btn outlined color="Genoa" small @click="openAddServiceModal = true">
        <v-icon left>
          mdi-plus-circle-outline
        </v-icon>
        Service</v-btn
      >
      <v-spacer></v-spacer>
      <span class="mr-2 search-text">篩選</span>
      <v-text-field
        v-model="search"
        hide-details
        outlined
        style="max-width:150px"
      ></v-text-field>
    </div>

    <v-data-table
      :headers="serviceHeaders"
      :items="serviceData"
      :search="search"
    >
      <template v-slot:item.serviceType="{ item }">
        <v-chip small>{{ item.serviceType }}</v-chip>
      </template>

      <template v-slot:item.postTest>
        <v-icon small @click="openAPITestModal = true">
          mdi-bug
        </v-icon>
      </template>
      <template v-slot:item.edit>
        <v-icon small @click="openEditServiceModal = true">
          mdi-square-edit-outline
        </v-icon>
      </template>
      <template v-slot:item.delete>
        <v-icon small @click="openIllegalDialog = true">
          mdi-delete
        </v-icon>
      </template>
      <template v-slot:item.detail>
        <v-icon small @click="openServiceDetailModal = true">
          mdi-magnify
        </v-icon>
      </template>
    </v-data-table>

    <title-bar issueTackerFilter="true">Issue Tracker</title-bar>
    <div class="d-flex align-center table-action">
      <v-spacer></v-spacer>
      <span class="mr-2 search-text">篩選</span>
      <v-text-field
        v-model="search"
        single-line
        hide-details
        outlined
        style="max-width:150px"
      ></v-text-field>
    </div>
    <v-data-table
      :headers="issueTrackerHeaders"
      :items="issueTrackerData"
      :search="search"
    >
      <template v-slot:item.edit>
        <v-icon small @click="openEditIssueModal = true">
          mdi-square-edit-outline
        </v-icon>
      </template>
    </v-data-table>

    <title-bar messageListFilter="true">Message List</title-bar>
    <div class="d-flex align-center table-action">
      <v-spacer></v-spacer>
      <span class="mr-2 search-text">篩選</span>
      <v-text-field
        v-model="search"
        single-line
        hide-details
        outlined
        style="max-width:150px"
      ></v-text-field>
    </div>
    <v-data-table
      :headers="messageListHeaders"
      :items="messageListData"
      :search="search"
    ></v-data-table>

    <add-service-modal
      :openModal="openAddServiceModal"
      @closeModal="openAddServiceModal = false"
    ></add-service-modal>
    <edit-service-modal
      :openModal="openEditServiceModal"
      @closeModal="openEditServiceModal = false"
    ></edit-service-modal>
    <notify-api-test-modal
      :openModal="openAPITestModal"
      @closeModal="openAPITestModal = false"
    ></notify-api-test-modal>
    <edit-issue-modal
      :openModal="openEditIssueModal"
      @closeModal="openEditIssueModal = false"
    ></edit-issue-modal>
    <service-detail-modal
      :openModal="openServiceDetailModal"
      @closeModal="openServiceDetailModal = false"
    ></service-detail-modal>

    <title-alert-dialog
      :openDialog="openIllegalDialog"
      @closeDialog="openIllegalDialog = false"
    >
      <template slot="title-icon">mdi-alert</template>
      <template slot="title-text">Illegal action</template>
      <template slot="content">
        <p>
          The Service you want to delete is in service for the past 30 days.
        </p>
        <p>*You can try to disable the service</p>
      </template>
      <template slot="action">
        <v-btn
          depressed
          color="DarkGray White--text"
          @click="openIllegalDialog = false"
          >取消</v-btn
        >
        <v-btn
          depressed
          color="FountainBlue White--text"
          @click="
            openIllegalDialog = false;
            openDeleteDialog = true;
          "
          >確定</v-btn
        >
      </template>
    </title-alert-dialog>
    <title-alert-dialog
      :openDialog="openDeleteDialog"
      @closeDialog="openDeleteDialog = false"
    >
      <template slot="title-icon">mdi-alert</template>
      <template slot="title-text">Delete</template>
      <template slot="content"
        >Are you sure to delete {{ deleteServicetId }} ?</template
      >
      <template slot="action">
        <v-btn
          depressed
          color="DarkGray White--text"
          @click="openDeleteDialog = false"
          >取消</v-btn
        >
        <v-btn
          depressed
          color="FountainBlue White--text"
          @click="
            openDeleteDialog = false;
            openConfirmDeleteDialog = true;
          "
          >確定</v-btn
        >
      </template>
    </title-alert-dialog>
    <alert-dialog
      :openDialog="openConfirmDeleteDialog"
      @closeDialog="openConfirmDeleteDialog = false"
    >
      <template slot="content">Delete Service successfully.</template>
      <template slot="action">
        <v-btn
          depressed
          color="FountainBlue White--text"
          @click="openConfirmDeleteDialog = false"
          >確定</v-btn
        >
      </template>
    </alert-dialog>
  </div>
</template>
<script>
  import TitleBar from "../components/TitleBar";
  import AddServiceModal from "../components/modals/AddService";
  import NotifyAPITestModal from "../components/modals/NotifyAPITest";
  import EditServiceModal from "../components/modals/EditService";
  import EditIssueModal from "../components/modals/EditIssue";
  import ServiceDetailModal from "../components/modals/ServiceDetail";
  import TitleAlertDialog from "../components/dialogs/TitleAlertDialog";
  import AlertDialog from "../components/dialogs/AlertDialog";

  export default {
    components: {
      "title-bar": TitleBar,
      "add-service-modal": AddServiceModal,
      "edit-service-modal": EditServiceModal,
      "edit-issue-modal": EditIssueModal,
      "notify-api-test-modal": NotifyAPITestModal,
      "service-detail-modal": ServiceDetailModal,
      "title-alert-dialog": TitleAlertDialog,
      "alert-dialog": AlertDialog,
    },
    data: () => {
      return {
        openAddServiceModal: false,
        openAPITestModal: false,
        openEditServiceModal: false,
        openDeleteDialog: false,
        openIllegalDialog: false,
        openConfirmDeleteDialog: false,
        openEditIssueModal: false,
        openServiceDetailModal: false,
        deleteServicetId: null,
        search: "",
        serviceHeaders: [
          {
            text: "Service ID",
            align: "start",
            value: "id",
          },
          { text: "Serv. Type", align: "center", value: "serviceType" },
          { text: "Serv. Desc.", align: "center d-none", value: "serviceDesc" },
          { text: "Project", align: "center", value: "project" },
          { text: "Tag", align: "center", value: "tag" },
          { text: "Channel", align: "center d-none", value: "channel" },
          { text: "Issue", align: "center", value: "issue" },
          //   { text: "Issue start time", value: "issueStartTime" },
          { text: "#Issue (Open)", align: "center", value: "booleanIssue" },
          { text: "#Fail (In 7 Days)", align: "center", value: "fail" },
          { text: "Recent activity", align: "center", value: "recentActivity" },
          { text: "Owner", align: "center", value: "owner" },
          { text: "Post Test", align: "center", value: "postTest" },
          { text: "Edit", align: "center", value: "edit" },
          { text: "Delete", align: "center", value: "delete" },
          { text: "Detail", align: "center", value: "detail" },
        ],
        serviceData: [
          {
            id: "id1",
            serviceType: "serviceType1",
            serviceDesc: "serviceDesc1",
            project: "project1",
            tag: "tag1",
            channel: "channel1",
            issue: "issue1",
            issueStartTime: "issueStartTime1",
            booleanIssue: "issue",
            fail: "fail",
            recentActivity: "recentActivity",
            owner: "owner",
          },
        ],
        issueTrackerHeaders: [
          { text: "Message ID", align: "center", value: "id" },
          { text: "Msg. Cont.", align: "center", value: "messageCont" },
          { text: "Link to Channel", align: "center", value: "linkToChannel" },
          { text: "Status", align: "center", value: "status" },
          { text: "Updated Time", align: "center", value: "updatedTime" },
          { text: "Edit", align: "center", value: "edit" },
        ],
        issueTrackerData: [
          {
            id: "11",
            messageCont: "messageCont1",
            linkToChannel: "linkToChannel1",
            status: "Open",
            updatedTime: "time",
          },
        ],
        messageListHeaders: [
          { text: "Message ID", align: "center", value: "id" },
          { text: "Msg. Cont.", align: "center", value: "messageCont" },
          { text: "API Response Type", align: "center", value: "type" },
          { text: "API Response", align: "center", value: "response" },
          { text: "Updated Time", align: "center", value: "updatedTime" },
        ],
        messageListData: [
          {
            id: "11",
            messageCont: "messageCont1",
            type: "type",
            response: "response",
            updatedTime: "time",
          },
        ],
      };
    },
  };
</script>
